<script>
document.addEventListener('DOMContentLoaded', function() {
  var toolbars = document.querySelectorAll('.price-id-toolbar');
  if (!toolbars.length) return;
  var CHA_BUY = {
    'lt5':    [2, 1],
    '6to7':   [3, 2],
    '8to10':  [4, 3],
    '11to15': [1, 1],
    '16to17': [3, 4],
    '18':     [2, 3],
    'ge19':   [1, 2]
  };
  var state = {cha: '11to15', sell: false, touristy: false, angry: false};

  // Populate each toolbar with the same compact button set.
  // Cha bracket on the left, then independent toggles: Sell, Tourist, Dunce.
  var btnHTML =
    '<span class="price-id-label">魅力</span>' +
    '<button data-group="cha" data-val="lt5">≤5</button>' +
    '<button data-group="cha" data-val="6to7">6-7</button>' +
    '<button data-group="cha" data-val="8to10">8-10</button>' +
    '<button data-group="cha" data-val="11to15">11-15</button>' +
    '<button data-group="cha" data-val="16to17">16-17</button>' +
    '<button data-group="cha" data-val="18">18</button>' +
    '<button data-group="cha" data-val="ge19">≥19</button>' +
    '<span class="price-id-sep">·</span>' +
    '<button data-group="toggle" data-val="sell">売却</button>' +
    '<button data-group="toggle" data-val="touristy">カモ</button>' +
    '<button data-group="toggle" data-val="angry">怒り</button>';
  toolbars.forEach(function(tb) {
    tb.innerHTML = btnHTML;
    tb.classList.add('price-id-widget');
  });

  function adj(base, m, d) {
    var n = base * m;
    if (d > 1) n = Math.floor((n * 10 / d + 5) / 10);
    return Math.max(1, n);
  }
  function computeBuy(base, surcharge) {
    // Replicates shk.c get_cost. Default Cha 11-15 no penalty: buy = base.
    var m = 1, d = 1;
    var cha = CHA_BUY[state.cha];
    m *= cha[0]; d *= cha[1];
    if (state.touristy) { m *= 4; d *= 3; }
    if (surcharge) { m *= 4; d *= 3; }
    var n = adj(base, m, d);
    // Angry-shopkeeper surcharge: added AFTER mult/div in shk.c:2986
    // (tmp + (tmp + 2) / 3, ~+33%). Stacks with Tourist. Buy-side only.
    if (state.angry) n = n + Math.floor((n + 2) / 3);
    return n;
  }
  function computeSell(base, unfamiliar) {
    // Replicates shk.c set_cost. Default no penalty: sell = base / 2.
    var m = 1, d = 1;
    if (state.touristy) d *= 3; else d *= 2;
    if (unfamiliar) { m *= 3; d *= 4; }
    return adj(base, m, d);
  }
  function pair(n1, n2) {
    return n1 === n2
      ? '' + n1
      : n1 + '<span class="pi-alt"> / ' + n2 + '</span>';
  }

  // Find every table whose first column header is "Price" or "価格". Stash the base
  // price (which is what shows initially, since default state quotes buy =
  // base) on each row's price cell. We also tolerate "Sell" or "売却" as a header
  // (e.g. after a previous render).
  var priceTables = [];
  document.querySelectorAll('table').forEach(function(t) {
    var hdrs = t.querySelectorAll('thead th');
    if (!hdrs.length) return;
    if (!/^(Price|Sell|価格|売却)$/i.test(hdrs[0].textContent.trim())) return;
    hdrs[0].classList.add('pi-col');
    t.querySelectorAll('tbody tr').forEach(function(tr) {
      var firstTd = tr.querySelector('td');
      if (!firstTd) return;
      var m = firstTd.textContent.trim().match(/^\$?(\d+)/);
      if (!m) return;
      if (!firstTd.dataset.basePrice) firstTd.dataset.basePrice = m[1];
      firstTd.classList.add('pi-price', 'pi-col');
    });
    priceTables.push(t);
  });

  function renderTables() {
    priceTables.forEach(function(t) {
      var hdr = t.querySelector('thead th.pi-col');
      if (hdr) hdr.textContent = state.sell ? '売却' : '価格';
      t.querySelectorAll('td.pi-price').forEach(function(td) {
        var base = parseInt(td.dataset.basePrice, 10);
        if (state.sell) {
          td.innerHTML = pair(computeSell(base, false), computeSell(base, true));
        } else {
          td.innerHTML = pair(computeBuy(base, false), computeBuy(base, true));
        }
      });
    });
  }

  function syncToolbars() {
    toolbars.forEach(function(tb) {
      tb.querySelectorAll('button[data-group="cha"]').forEach(function(b) {
        b.classList.toggle('active', b.dataset.val === state.cha);
      });
      tb.querySelectorAll('button[data-group="toggle"]').forEach(function(b) {
        b.classList.toggle('active', !!state[b.dataset.val]);
      });
    });
  }

  toolbars.forEach(function(tb) {
    tb.addEventListener('click', function(ev) {
      var btn = ev.target.closest('button');
      if (!btn) return;
      var g = btn.dataset.group, v = btn.dataset.val;
      if (g === 'cha') state.cha = v;
      else state[v] = !state[v];
      syncToolbars();
      renderTables();
    });
  });

  syncToolbars();
  renderTables();
});
</script>
