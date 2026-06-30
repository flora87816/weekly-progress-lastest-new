<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Weekly Progress Report</title>
<style>
  :root {
    --bg: #0f1117;
    --surface: #1a1d27;
    --surface2: #222636;
    --border: #2d3148;
    --accent: #6366f1;
    --accent2: #818cf8;
    --green: #22c55e;
    --red: #ef4444;
    --yellow: #f59e0b;
    --text: #e2e8f0;
    --text2: #94a3b8;
    --text3: #64748b;
    --hpp: #3b82f6;
    --htl: #f59e0b;
    --sht: #a855f7;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { background: var(--bg); color: var(--text); font-family: -apple-system, 'Segoe UI', sans-serif; font-size: 13px; min-height: 100vh; }
  .header { background: var(--surface); border-bottom: 1px solid var(--border); padding: 16px 24px; display: flex; align-items: center; justify-content: space-between; position: sticky; top: 0; z-index: 100; }
  .header-logo { display: flex; align-items: center; gap: 10px; }
  .logo-icon { width: 32px; height: 32px; background: var(--accent); border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 16px; }
  .header h1 { font-size: 16px; font-weight: 700; }
  .header-meta { color: var(--text3); font-size: 12px; }
  .week-badge { background: var(--accent); color: #fff; padding: 3px 10px; border-radius: 12px; font-size: 11px; font-weight: 600; }
  .tabs { display: flex; gap: 2px; background: var(--surface); padding: 0 24px; border-bottom: 1px solid var(--border); overflow-x: auto; }
  .tab { padding: 12px 16px; cursor: pointer; font-size: 13px; font-weight: 500; color: var(--text3); border-bottom: 2px solid transparent; white-space: nowrap; transition: all 0.15s; }
  .tab:hover { color: var(--text); }
  .tab.active { color: var(--accent2); border-bottom-color: var(--accent); }
  .content { padding: 20px 24px; max-width: 1400px; margin: 0 auto; }
  .section { display: none; }
  .section.active { display: block; }
  .section-title { font-size: 15px; font-weight: 700; margin-bottom: 16px; display: flex; align-items: center; gap: 8px; }
  .section-title::before { content: ""; width: 4px; height: 16px; background: var(--accent); border-radius: 2px; display: block; }
  .table-wrap { overflow-x: auto; border-radius: 8px; border: 1px solid var(--border); margin-bottom: 20px; }
  table { width: 100%; border-collapse: collapse; }
  thead tr { background: var(--surface2); }
  thead th { padding: 8px 12px; text-align: right; font-weight: 600; font-size: 11px; color: var(--text2); white-space: nowrap; }
  thead th:first-child { text-align: left; }
  thead th.col-group { text-align: center; border-bottom: 1px solid var(--border); }
  thead th.col-w1 { color: var(--text2) !important; }
  thead th.col-w2 { color: var(--accent2) !important; }
  thead th.col-wow { color: var(--yellow) !important; }
  tbody tr { border-top: 1px solid var(--border); transition: background 0.1s; }
  tbody tr:hover { background: rgba(99,102,241,0.05); }
  tbody td { padding: 7px 12px; text-align: right; white-space: nowrap; }
  tbody td:first-child { text-align: left; color: var(--text2); font-weight: 500; }
  .row-city td { background: rgba(99,102,241,0.06); }
  .row-city td:first-child { color: var(--text); font-weight: 700; }
  .row-star td:first-child { padding-left: 28px; color: var(--text3); font-size: 12px; }
  .row-total { border-top: 2px solid var(--border) !important; }
  .row-total td { font-weight: 600; background: var(--surface2); color: var(--text) !important; }
  .wow-up { color: var(--green); }
  .wow-dn { color: var(--red); }
  .wow-nt { color: var(--text3); }
  .num-rn { color: var(--text); }
  .num-rev { color: var(--text2); }
  .num-adr { color: var(--accent2); }
  .summary-row { display: flex; gap: 10px; margin-bottom: 20px; flex-wrap: wrap; }
  .summary-card { flex: 1; min-width: 130px; background: var(--surface); border: 1px solid var(--border); border-radius: 8px; padding: 12px 16px; }
  .summary-card-label { font-size: 10px; color: var(--text3); margin-bottom: 4px; text-transform: uppercase; letter-spacing: 0.5px; }
  .summary-card-value { font-size: 18px; font-weight: 700; }
  .summary-card-wow { font-size: 11px; margin-top: 2px; }
  .city-tabs { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 16px; }
  .city-tab { padding: 5px 12px; border-radius: 16px; border: 1px solid var(--border); background: var(--surface); color: var(--text3); cursor: pointer; font-size: 12px; font-weight: 500; transition: all 0.15s; }
  .city-tab:hover { border-color: var(--accent); color: var(--text); }
  .city-tab.active { background: var(--accent); border-color: var(--accent); color: #fff; }
  .ez-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 12px; }
  .ez-card { background: var(--surface); border: 1px solid var(--border); border-radius: 10px; padding: 16px; }
  .ez-card-title { font-size: 14px; font-weight: 700; margin-bottom: 2px; }
  .ez-card-total { font-size: 11px; color: var(--text3); margin-bottom: 14px; }
  .ez-row { margin-bottom: 12px; }
  .ez-label { display: flex; justify-content: space-between; margin-bottom: 5px; font-size: 11px; }
  .ez-type-hpp { color: var(--hpp); font-weight: 700; }
  .ez-type-htl { color: var(--htl); font-weight: 700; }
  .ez-type-sht { color: var(--sht); font-weight: 700; }
  .ez-bar-track { position: relative; height: 20px; background: var(--surface2); border-radius: 4px; overflow: hidden; border: 1px solid var(--border); }
  .ez-bar-w1 { position: absolute; top: 0; left: 0; height: 50%; opacity: 0.5; border-radius: 4px 4px 0 0; }
  .ez-bar-w2 { position: absolute; bottom: 0; left: 0; height: 50%; border-radius: 0 0 4px 4px; }
  .fill-hpp { background: var(--hpp); }
  .fill-htl { background: var(--htl); }
  .fill-sht { background: var(--sht); }
  .ez-pct-row { display: flex; justify-content: space-between; margin-top: 3px; font-size: 10px; color: var(--text3); }
  .ez-pct-wow { font-weight: 600; }
  .pct-up { color: var(--green); }
  .pct-dn { color: var(--red); }
</style>
</head>
<body>

<div class="header">
  <div class="header-logo">
    <div class="logo-icon">📊</div>
    <div>
      <h1>Weekly Progress Report</h1>
      <div class="header-meta" id="reportMeta"></div>
    </div>
  </div>
  <span class="week-badge" id="weekBadge"></span>
</div>

<div class="tabs">
  <div class="tab active" onclick="showSection('mm',this)">MM 概況</div>
  <div class="tab" onclick="showSection('city',this)">城市 &amp; 星級</div>
  <div class="tab" onclick="showSection('site',this)">各國籍概況</div>
  <div class="tab" onclick="showSection('ez',this)">EZ Share</div>
</div>

<div class="content">
  <div class="section active" id="sec-mm">
    <div class="section-title">MM 概況</div>
    <div class="summary-row" id="mm-summary"></div>
    <div class="table-wrap">
      <table>
        <thead>
          <tr>
            <th rowspan="2">MM</th>
            <th colspan="3" class="col-group col-w1" id="lbl-w1-mm"></th>
            <th colspan="3" class="col-group col-w2" id="lbl-w2-mm"></th>
            <th colspan="3" class="col-group col-wow">WoW</th>
          </tr>
          <tr>
            <th>RN</th><th>REV</th><th>ADR</th>
            <th>RN</th><th>REV</th><th>ADR</th>
            <th>RN</th><th>REV</th><th>ADR</th>
          </tr>
        </thead>
        <tbody id="mm-tbody"></tbody>
      </table>
    </div>
  </div>

  <div class="section" id="sec-city">
    <div class="section-title">城市 &amp; 星級概況</div>
    <div class="table-wrap">
      <table>
        <thead>
          <tr>
            <th rowspan="2">城市 / 星級</th>
            <th colspan="3" class="col-group col-w1" id="lbl-w1-city"></th>
            <th colspan="3" class="col-group col-w2" id="lbl-w2-city"></th>
            <th colspan="3" class="col-group col-wow">WoW</th>
          </tr>
          <tr>
            <th>RN</th><th>REV</th><th>ADR</th>
            <th>RN</th><th>REV</th><th>ADR</th>
            <th>RN</th><th>REV</th><th>ADR</th>
          </tr>
        </thead>
        <tbody id="city-tbody"></tbody>
      </table>
    </div>
  </div>

  <div class="section" id="sec-site">
    <div class="section-title">各國籍概況</div>
    <div class="city-tabs" id="site-city-tabs"></div>
    <div class="table-wrap">
      <table>
        <thead>
          <tr>
            <th rowspan="2">Site</th>
            <th colspan="3" class="col-group col-w1" id="lbl-w1-site"></th>
            <th colspan="3" class="col-group col-w2" id="lbl-w2-site"></th>
            <th colspan="3" class="col-group col-wow">WoW</th>
          </tr>
          <tr>
            <th>RN</th><th>REV</th><th>ADR</th>
            <th>RN</th><th>REV</th><th>ADR</th>
            <th>RN</th><th>REV</th><th>ADR</th>
          </tr>
        </thead>
        <tbody id="site-tbody"></tbody>
      </table>
    </div>
  </div>

  <div class="section" id="sec-ez">
    <div class="section-title">EZ Share</div>
    <div class="ez-grid" id="ez-grid"></div>
  </div>
</div>

<script>
const D = {"report_date":"2026-06-29","week1_label":"6/12-6/18","week2_label":"6/19-6/25","mm_overview":[{"name":"Abby Cheng （鄭任妤）","w1_rn":7133,"w1_rev":4445354.36,"w1_adr":623.21,"w2_rn":7673,"w2_rev":4688536.1,"w2_adr":611.04,"wow_rn":0.0757044721715968,"wow_rev":0.05470469027959204,"wow_adr":-0.019521887688735872},{"name":"Hino Chi （籍喆）","w1_rn":10539,"w1_rev":4262339.58,"w1_adr":404.43,"w2_rn":10362,"w2_rev":4397551.91,"w2_adr":424.39,"wow_rn":-0.016794762311414746,"wow_rev":0.03172256243945127,"wow_adr":0.049346080442904526},{"name":"Sandy Su （蘇筱鈞）","w1_rn":8874,"w1_rev":6906078.12,"w1_adr":778.24,"w2_rn":9564,"w2_rev":7508527.53,"w2_adr":785.08,"wow_rn":0.0777552400270453,"wow_rev":0.08723466429373554,"wow_adr":0.008795526029131062},{"name":"Wayne Wang （王俊明）","w1_rn":2400,"w1_rev":1811961.73,"w1_adr":754.98,"w2_rn":2411,"w2_rev":1862283.76,"w2_adr":772.41,"wow_rn":0.004583333333333333,"wow_rev":0.02777212643815097,"wow_adr":0.02308299603963599},{"name":"Carol Lin （林芝榕）","w1_rn":3830,"w1_rev":3281949.36,"w1_adr":856.91,"w2_rn":4202,"w2_rev":3552934.59,"w2_adr":845.53,"wow_rn":0.09712793733681462,"wow_rev":0.08256837624607875,"wow_adr":-0.013270613750004448},{"name":"Flora Tsao （曹芳綺）","w1_rn":809,"w1_rev":428991.59,"w1_adr":530.27,"w2_rn":807,"w2_rev":403663.75,"w2_adr":500.2,"wow_rn":-0.002472187886279357,"wow_rev":-0.0590404252576032,"wow_adr":-0.05670843126815492},{"name":"Justin Lee （李岳勳）","w1_rn":3522,"w1_rev":3031681.55,"w1_adr":860.78,"w2_rn":4199,"w2_rev":3790871.44,"w2_adr":902.8,"wow_rn":0.19222032935831915,"wow_rev":0.2504187444998846,"wow_adr":0.048815150780803306}],"city_star_overview":[{"city":"台中","w1_rn":11364,"w1_rev":6023987.33,"w1_adr":530.09,"w2_rn":11375,"w2_rev":5818182.62,"w2_adr":511.49,"wow_rn":0.0009679690249912002,"wow_rev":-0.03416420032378558,"wow_adr":-0.035098195382813266,"stars":[{"star":3,"w1_rn":5861,"w1_rev":2219831.73,"w1_adr":378.75,"w2_rn":5664,"w2_rev":2109789.04,"w2_adr":372.49,"wow_rn":-0.03361201160211568,"wow_rev":-0.04957253874173093,"wow_adr":-0.016515651406300312},{"star":4,"w1_rn":4394,"w1_rev":2546502.42,"w1_adr":579.54,"w2_rn":4511,"w2_rev":2485692.84,"w2_adr":551.03,"wow_rn":0.026627218934911243,"wow_rev":-0.023879649996417687,"wow_adr":-0.04919689250371522},{"star":5,"w1_rn":1109,"w1_rev":1257653.17,"w1_adr":1134.04,"w2_rn":1200,"w2_rev":1222700.74,"w2_adr":1018.92,"wow_rn":0.08205590622182146,"wow_rev":-0.027791786685482316,"wow_adr":-0.10151757619516658}]},{"city":"台東","w1_rn":2543,"w1_rev":1826746.49,"w1_adr":718.34,"w2_rn":2775,"w2_rev":1981263.31,"w2_adr":713.97,"wow_rn":0.09123082972866693,"wow_rev":0.08458580300278704,"wow_adr":-0.006089478545554096,"stars":[{"star":3,"w1_rn":1250,"w1_rev":634260.34,"w1_adr":507.41,"w2_rn":1452,"w2_rev":749318.88,"w2_adr":516.06,"wow_rn":0.1616,"wow_rev":0.1814058623511157,"wow_adr":0.017050501335326866},{"star":4,"w1_rn":997,"w1_rev":809516.07,"w1_adr":811.95,"w2_rn":976,"w2_rev":807001.38,"w2_adr":826.85,"wow_rn":-0.02106318956870612,"wow_rev":-0.0031064176403554932,"wow_adr":0.018343136898120466},{"star":5,"w1_rn":296,"w1_rev":382970.08,"w1_adr":1293.82,"w2_rn":347,"w2_rev":424943.05,"w2_adr":1224.62,"wow_rn":0.17229729729729729,"wow_rev":0.10959856185109859,"wow_adr":-0.05348364752759312}]},{"city":"台南","w1_rn":5040,"w1_rev":3199023.14,"w1_adr":634.73,"w2_rn":5629,"w2_rev":3621314.91,"w2_adr":643.33,"wow_rn":0.11686507936507937,"wow_rev":0.13200647435529322,"wow_adr":0.013557049342810008,"stars":[{"star":3,"w1_rn":1949,"w1_rev":1005904.06,"w1_adr":516.11,"w2_rn":2039,"w2_rev":972274.27,"w2_adr":476.84,"wow_rn":0.046177526936890714,"wow_rev":-0.033432399328774655,"wow_adr":-0.07609600112397345},{"star":4,"w1_rn":2365,"w1_rev":1404035.92,"w1_adr":593.67,"w2_rn":2597,"w2_rev":1560049.37,"w2_adr":600.71,"wow_rn":0.09809725158562368,"wow_rev":0.11111784233331118,"wow_adr":0.01185741128928809},{"star":5,"w1_rn":726,"w1_rev":789083.16,"w1_adr":1086.89,"w2_rn":993,"w2_rev":1088991.27,"w2_adr":1096.67,"wow_rn":0.3677685950413223,"wow_rev":0.3800716134431155,"wow_adr":0.00899495605206635}]},{"city":"花蓮","w1_rn":2072,"w1_rev":1350556.93,"w1_adr":651.81,"w2_rn":2524,"w2_rev":1759788.82,"w2_adr":697.22,"wow_rn":0.21814671814671815,"wow_rev":0.3030097243997589,"wow_adr":0.06966566915859752,"stars":[{"star":3,"w1_rn":1158,"w1_rev":460336.81,"w1_adr":397.53,"w2_rn":1367,"w2_rev":553755.59,"w2_adr":405.09,"wow_rn":0.18048359240069084,"wow_rev":0.20293571574320393,"wow_adr":0.019019428552033646},{"star":4,"w1_rn":617,"w1_rev":400278.58,"w1_adr":648.75,"w2_rn":668,"w2_rev":465164.21,"w2_adr":696.35,"wow_rn":0.08265802269043761,"wow_rev":0.1621011627467993,"wow_adr":0.07337787038139995},{"star":5,"w1_rn":297,"w1_rev":489941.54,"w1_adr":1649.63,"w2_rn":489,"w2_rev":740869.02,"w2_adr":1515.07,"wow_rn":0.6464646464646465,"wow_rev":0.5121580017485349,"wow_adr":-0.08157274740426412}]},{"city":"金門","w1_rn":472,"w1_rev":269998.45,"w1_adr":572.03,"w2_rn":377,"w2_rev":210964.64,"w2_adr":559.59,"wow_rn":-0.20127118644067796,"wow_rev":-0.21864499613338928,"wow_adr":-0.021751825397771235,"stars":[{"star":3,"w1_rn":411,"w1_rev":234635.06,"w1_adr":570.89,"w2_rn":309,"w2_rev":173338.77,"w2_adr":560.97,"wow_rn":-0.24817518248175183,"wow_rev":-0.2612409673462777,"wow_adr":-0.017378762392621806},{"star":4,"w1_rn":61,"w1_rev":35363.39,"w1_adr":579.73,"w2_rn":68,"w2_rev":37625.87,"w2_adr":553.32,"wow_rn":0.11475409836065574,"wow_rev":0.06397802925567884,"wow_adr":-0.04554912081475866}]},{"city":"南投","w1_rn":1316,"w1_rev":1484367.2,"w1_adr":1127.94,"w2_rn":1597,"w2_rev":1781287.68,"w2_adr":1115.4,"wow_rn":0.2135258358662614,"wow_rev":0.20003168582538355,"wow_adr":-0.011119788011142996,"stars":[{"star":2,"w1_rn":4,"w1_rev":2307.36,"w1_adr":576.84,"w2_rn":1,"w2_rev":367.3,"w2_adr":367.3,"wow_rn":-0.75,"wow_rev":-0.8408137438457804,"wow_adr":-0.36325497538312174},{"star":3,"w1_rn":696,"w1_rev":562576.33,"w1_adr":808.3,"w2_rn":803,"w2_rev":625230.98,"w2_adr":778.62,"wow_rn":0.15373563218390804,"wow_rev":0.11137093165650849,"wow_adr":-0.03671959099261535},{"star":4,"w1_rn":421,"w1_rev":413404.99,"w1_adr":981.96,"w2_rn":582,"w2_rev":586816.43,"w2_adr":1008.28,"wow_rn":0.3824228028503563,"wow_rev":0.41947106816873864,"wow_adr":0.026799518383228516},{"star":5,"w1_rn":195,"w1_rev":506078.52,"w1_adr":2595.27,"w2_rn":211,"w2_rev":568872.97,"w2_adr":2696.08,"wow_rn":0.08205128205128205,"wow_rev":0.12408044901806901,"wow_adr":0.038842121130443004}]},{"city":"屏東","w1_rn":1170,"w1_rev":1498422.08,"w1_adr":1280.7,"w2_rn":1135,"w2_rev":1537310.54,"w2_adr":1354.46,"wow_rn":-0.029914529914529916,"wow_rev":0.0259529429889145,"wow_adr":0.05759025841148011,"stars":[{"star":3,"w1_rn":356,"w1_rev":265262.68,"w1_adr":745.12,"w2_rn":270,"w2_rev":202824.65,"w2_adr":751.2,"wow_rn":-0.24157303370786518,"wow_rev":-0.23538186873417866,"wow_adr":0.008163165669008914},{"star":4,"w1_rn":184,"w1_rev":207909.87,"w1_adr":1129.94,"w2_rn":180,"w2_rev":209419.69,"w2_adr":1163.44,"wow_rn":-0.021739130434782608,"wow_rev":0.0072618821714151745,"wow_adr":0.02964547955300205},{"star":5,"w1_rn":630,"w1_rev":1025249.53,"w1_adr":1627.38,"w2_rn":685,"w2_rev":1125066.2,"w2_adr":1642.43,"wow_rn":0.0873015873015873,"wow_rev":0.09735841606260952,"wow_adr":0.009249346159772194}]},{"city":"高雄","w1_rn":11034,"w1_rev":7083896.81,"w1_adr":642.01,"w2_rn":11821,"w2_rev":8112175.1,"w2_adr":686.25,"wow_rn":0.07132499546855176,"wow_rev":0.14515715257663234,"wow_adr":0.06891667553764999,"stars":[{"star":3,"w1_rn":5425,"w1_rev":2496136.53,"w1_adr":460.12,"w2_rn":5710,"w2_rev":2906818.35,"w2_adr":509.08,"wow_rn":0.052534562211981564,"wow_rev":0.16452698735181912,"wow_adr":0.10640261057506462},{"star":4,"w1_rn":4542,"w1_rev":3094646.82,"w1_adr":681.34,"w2_rn":4974,"w2_rev":3540688.8,"w2_adr":711.84,"wow_rn":0.095112285336856,"wow_rev":0.14413340311088302,"wow_adr":0.04476355386602944},{"star":5,"w1_rn":1067,"w1_rev":1493113.47,"w1_adr":1399.36,"w2_rn":1137,"w2_rev":1664667.96,"w2_adr":1464.09,"wow_rn":0.06560449859418932,"wow_rev":0.11489715555584742,"wow_adr":0.046257928740623774}]},{"city":"嘉義","w1_rn":2096,"w1_rev":1431357.87,"w1_adr":682.9,"w2_rn":1985,"w2_rev":1382081.47,"w2_adr":696.26,"wow_rn":-0.05295801526717557,"wow_rev":-0.034426331121556554,"wow_adr":0.01956796472000881,"stars":[{"star":3,"w1_rn":778,"w1_rev":390262.62,"w1_adr":501.62,"w2_rn":711,"w2_rev":351983.69,"w2_adr":495.05,"wow_rn":-0.08611825192802057,"wow_rev":-0.09808505336690636,"wow_adr":-0.013094474710904566},{"star":4,"w1_rn":1125,"w1_rev":793553.22,"w1_adr":705.38,"w2_rn":1102,"w2_rev":789981.73,"w2_adr":716.86,"wow_rn":-0.020444444444444446,"wow_rev":-0.004500630594693774,"wow_adr":0.016276579474563888},{"star":5,"w1_rn":193,"w1_rev":247542.03,"w1_adr":1282.6,"w2_rn":172,"w2_rev":240116.05,"w2_adr":1396.02,"wow_rn":-0.10880829015544041,"wow_rev":-0.029998865925909137,"wow_adr":0.08843150509476475}]}],"city_site_overview":{"台中":{"sites":[{"site":"Trip(AE)","w1_rn":2,"w1_rev":585.68,"w1_adr":292.84,"w2_rn":0,"w2_rev":0.0,"w2_adr":0,"wow_rn":-1.0,"wow_rev":-1.0,"wow_adr":-1.0},{"site":"Trip(AU)","w1_rn":54,"w1_rev":27520.35,"w1_adr":509.64,"w2_rn":14,"w2_rev":5077.53,"w2_adr":362.68,"wow_rn":-0.7407407407407407,"wow_rev":-0.8154990761382033,"wow_adr":-0.28835357939021244},{"site":"Trip(BE)","w1_rn":1,"w1_rev":553.01,"w1_adr":553.01,"w2_rn":0,"w2_rev":0.0,"w2_adr":0,"wow_rn":-1.0,"wow_rev":-1.0,"wow_adr":-1.0},{"site":"Trip(CA)","w1_rn":21,"w1_rev":10334.06,"w1_adr":492.1,"w2_rn":12,"w2_rev":6196.66,"w2_adr":516.39,"wow_rn":-0.42857142857142855,"wow_rev":-0.4003653936594137,"wow_adr":0.04936056109602597},{"site":"Trip(CH)","w1_rn":1,"w1_rev":245.85,"w1_adr":245.85,"w2_rn":0,"w2_rev":0.0,"w2_adr":0,"wow_rn":-1.0,"wow_rev":-1.0,"wow_adr":-1.0},{"site":"Trip(CN1)","w1_rn":3340,"w1_rev":1992999.56,"w1_adr":596.71,"w2_rn":3594,"w2_rev":1927935.86,"w2_adr":536.43,"wow_rn":0.07604790419161676,"wow_rev":-0.03264611839713698,"wow_adr":-0.10101225248927018},{"site":"Trip(DE)","w1_rn":7,"w1_rev":4099.31,"w1_adr":585.62,"w2_rn":6,"w2_rev":1849.78,"w2_adr":308.3,"wow_rn":-0.14285714285714285,"wow_rev":-0.5487582056492434,"wow_adr":-0.47355123992411724},{"site":"Trip(DK)","w1_rn":0,"w1_rev":0.0,"w1_adr":0,"w2_rn":2,"w2_rev":2138.92,"w2_adr":1069.46,"wow_rn":null,"wow_rev":null,"wow_adr":null},{"site":"Trip(ES)","w1_rn":7,"w1_rev":3071.03,"w1_adr":438.72,"w2_rn":2,"w2_rev":606.58,"w2_adr":303.29,"wow_rn":-0.7142857142857143,"wow_rev":-0.8024832059602153,"wow_adr":-0.30869122086075346},{"site":"Trip(FR)","w1_rn":5,"w1_rev":1492.91,"w1_adr":298.58,"w2_rn":4,"w2_rev":1022.32,"w2_adr":255.58,"wow_rn":-0.2,"wow_rev":-0.3152165904173729,"wow_adr":-0.144020738021716},{"site":"Trip(GB)","w1_rn":36,"w1_rev":12159.42,"w1_adr":337.76,"w2_rn":36,"w2_rev":17317.48,"w2_adr":481.04,"wow_rn":0.0,"wow_rev":0.4242027991466698,"wow_adr":0.4242027991466698},{"site":"Trip(HK)","w1_rn":1694,"w1_rev":867727.7,"w1_adr":512.24,"w2_rn":1375,"w2_rev":731379.66,"w2_adr":531.91,"wow_rn":-0.18831168831168832,"wow_rev":-0.157132288718841,"wow_adr":0.03841302029838798},{"site":"Trip(ID)","w1_rn":206,"w1_rev":81052.65,"w1_adr":393.46,"w2_rn":182,"w2_rev":80410.89,"w2_adr":441.82,"wow_rn":-0.11650485436893204,"wow_rev":-0.007917816382314218,"wow_adr":0.12290620783100688},{"site":"Trip(IN)","w1_rn":4,"w1_rev":697.94,"w1_adr":174.49,"w2_rn":2,"w2_rev":1509.48,"w2_adr":754.74,"wow_rn":-0.5,"wow_rev":1.1627647075679857,"wow_adr":3.3255294151359713},{"site":"Trip(IT)","w1_rn":0,"w1_rev":0.0,"w1_adr":0,"w2_rn":1,"w2_rev":722.24,"w2_adr":722.24,"wow_rn":null,"wow_rev":null,"wow_adr":null},{"site":"Trip(JP)","w1_rn":260,"w1_rev":94468.72,"w1_adr":363.34,"w2_rn":282,"w2_rev":112529.31,"w2_adr":399.04,"wow_rn":0.08461538461538462,"wow_rev":0.19118063629950754,"wow_adr":0.09825165048890763},{"site":"Trip(KR)","w1_rn":246,"w1_rev":123957.21,"w1_adr":503.89,"w2_rn":195,"w2_rev":71551.41,"w2_adr":366.93,"wow_rn":-0.2073170731707317,"wow_rev":-0.4227733102414936,"wow_adr":-0.27180632984311504},{"site":"Trip(MY)","w1_rn":369,"w1_rev":146562.22,"w1_adr":397.19,"w2_rn":354,"w2_rev":143334.42,"w2_adr":404.9,"wow_rn":-0.04065040650406504,"wow_rev":-0.022023410944512486,"wow_adr":0.019416275032415078},{"site":"Trip(NL)","w1_rn":10,"w1_rev":1532.32,"w1_adr":153.23,"w2_rn":0,"w2_rev":0.0,"w2_adr":0,"wow_rn":-1.0,"wow_rev":-1.0,"wow_adr":-1.0},{"site":"Trip(NZ)","w1_rn":4,"w1_rev":1151.06,"w1_adr":287.76,"w2_rn":0,"w2_rev":0.0,"w2_adr":0,"wow_rn":-1.0,"wow_rev":-1.0,"wow_adr":-1.0},{"site":"Trip(PH)","w1_rn":83,"w1_rev":21822.33,"w1_adr":262.92,"w2_rn":72,"w2_rev":28013.85,"w2_adr":389.08,"wow_rn":-0.13253012048192772,"wow_rev":0.2837239653144285,"wow_adr":0.47984846001524395},{"site":"Trip(RU)","w1_rn":13,"w1_rev":5496.8,"w1_adr":422.83,"w2_rn":4,"w2_rev":2378.14,"w2_adr":594.53,"wow_rn":-0.6923076923076923,"wow_rev":-0.5673591908019212,"wow_adr":0.4060826298937562},{"site":"Trip(SG)","w1_rn":371,"w1_rev":201016.91,"w1_adr":541.82,"w2_rn":406,"w2_rev":228130.79,"w2_adr":561.9,"wow_rn":0.09433962264150944,"wow_rev":0.13488355681121572,"wow_adr":0.037048767430938365},{"site":"Trip(TH)","w1_rn":94,"w1_rev":34341.63,"w1_adr":365.34,"w2_rn":99,"w2_rev":29211.25,"w2_adr":295.06,"wow_rn":0.05319148936170213,"wow_rev":-0.14939235266351675,"wow_adr":-0.19235233485222808},{"site":"Trip(TW)","w1_rn":4287,"w1_rev":2290938.13,"w1_adr":534.39,"w2_rn":4459,"w2_rev":2308330.56,"w2_adr":517.68,"wow_rn":0.04012129694425006,"wow_rev":0.007591838386788918,"wow_adr":-0.03127467791788202},{"site":"Trip(US)","w1_rn":60,"w1_rev":22420.74,"w1_adr":373.68,"w2_rn":87,"w2_rev":37625.66,"w2_adr":432.48,"wow_rn":0.45,"wow_rev":0.6781631649981232,"wow_adr":0.15735390689525738},{"site":"Trip(VN)","w1_rn":28,"w1_rev":7162.81,"w1_adr":255.81,"w2_rn":34,"w2_rev":10923.32,"w2_adr":321.27,"wow_rn":0.21428571428571427,"wow_rev":0.5250052797051459,"wow_adr":0.2558867009336495},{"site":"Trip(XX)","w1_rn":161,"w1_rev":70576.98,"w1_adr":438.37,"w2_rn":153,"w2_rev":69986.51,"w2_adr":457.43,"wow_rn":-0.049689440993788817,"wow_rev":-0.008366325677295927,"wow_adr":0.04348380108467553}],"total_w1_rn":11364,"total_w2_rn":11375},"台東":{"sites":[{"site":"Trip(AU)","w1_rn":0,"w1_rev":0.0,"w1_adr":0,"w2_rn":6,"w2_rev":5605.34,"w2_adr":934.22,"wow_rn":null,"wow_rev":null,"wow_adr":null},{"site":"Trip(CA)","w1_rn":6,"w1_rev":3998.57,"w1_adr":666.43,"w2_rn":0,"w2_rev":0.0,"w2_adr":0,"wow_rn":-1.0,"wow_rev":-1.0,"wow_adr":-1.0},{"site":"Trip(CN1)","w1_rn":1323,"w1_rev":1009911.16,"w1_adr":763.35,"w2_rn":1358,"w2_rev":1000842.8,"w2_adr":737.0,"wow_rn":0.026455026455026454,"wow_rev":-0.008979364184865236,"wow_adr":-0.03452113314917281},{"site":"Trip(DE)","w1_rn":7,"w1_rev":1911.5,"w1_adr":273.07,"w2_rn":0,"w2_rev":0.0,"w2_adr":0,"wow_rn":-1.0,"wow_rev":-1.0,"wow_adr":-1.0},{"site":"Trip(DK)","w1_rn":0,"w1_rev":0.0,"w1_adr":0,"w2_rn":2,"w2_rev":2147.08,"w2_adr":1073.54,"wow_rn":null,"wow_rev":null,"wow_adr":null},{"site":"Trip(ES)","w1_rn":0,"w1_rev":0.0,"w1_adr":0,"w2_rn":3,"w2_rev":1453.99,"w2_adr":484.66,"wow_rn":null,"wow_rev":null,"wow_adr":null},{"site":"Trip(FR)","w1_rn":0,"w1_rev":0.0,"w1_adr":0,"w2_rn":5,"w2_rev":944.42,"w2_adr":188.88,"wow_rn":null,"wow_rev":null,"wow_adr":null},{"site":"Trip(GB)","w1_rn":6,"w1_rev":4358.54,"w1_adr":726.42,"w2_rn":0,"w2_rev":0.0,"w2_adr":0,"wow_rn":-1.0,"wow_rev":-1.0,"wow_adr":-1.0},{"site":"Trip(HK)","w1_rn":110,"w1_rev":63158.17,"w1_adr":574.17,"w2_rn":201,"w2_rev":139036.22,"w2_adr":691.72,"wow_rn":0.8272727272727273,"wow_rev":1.2013970479672667,"wow_adr":0.20474465311641454},{"site":"Trip(ID)","w1_rn":0,"w1_rev":0.0,"w1_adr":0,"w2_rn":3,"w2_rev":1136.57,"w2_adr":378.86,"wow_rn":null,"wow_rev":null,"wow_adr":null},{"site":"Trip(IL)","w1_rn":1,"w1_rev":446.45,"w1_adr":446.45,"w2_rn":2,"w2_rev":408.83,"w2_adr":204.41,"wow_rn":1.0,"wow_rev":-0.08426475529174601,"wow_adr":-0.542132377645873},{"site":"Trip(IT)","w1_rn":0,"w1_rev":0.0,"w1_adr":0,"w2_rn":1,"w2_rev":119.01,"w2_adr":119.01,"wow_rn":null,"wow_rev":null,"wow_adr":null},{"site":"Trip(JP)","w1_rn":18,"w1_rev":8553.51,"w1_adr":475.19,"w2_rn":14,"w2_rev":8880.72,"w2_adr":634.34,"wow_rn":-0.2222222222222222,"wow_rev":0.03825447097156617,"wow_adr":0.3348986055348708},{"site":"Trip(KR)","w1_rn":3,"w1_rev":4578.22,"w1_adr":1526.07,"w2_rn":7,"w2_rev":3764.68,"w2_adr":537.81,"wow_rn":1.3333333333333333,"wow_rev":-0.17769788258318733,"wow_adr":-0.6475848068213661},{"site":"Trip(MY)","w1_rn":19,"w1_rev":10897.1,"w1_adr":573.53,"w2_rn":20,"w2_rev":7007.24,"w2_adr":350.36,"wow_rn":0.05263157894736842,"wow_rev":-0.3569628616787953,"wow_adr":-0.3891147185948556},{"site":"Trip(NL)","w1_rn":1,"w1_rev":386.5,"w1_adr":386.5,"w2_rn":0,"w2_rev":0.0,"w2_adr":0,"wow_rn":-1.0,"wow_rev":-1.0,"wow_adr":-1.0},{"site":"Trip(NZ)","w1_rn":0,"w1_rev":0.0,"w1_adr":0,"w2_rn":1,"w2_rev":559.45,"w2_adr":559.45,"wow_rn":null,"wow_rev":null,"wow_adr":null},{"site":"Trip(PH)","w1_rn":1,"w1_rev":421.15,"w1_adr":421.15,"w2_rn":3,"w2_rev":1616.06,"w2_adr":538.69,"wow_rn":2.0,"wow_rev":2.8372551347500887,"wow_adr":0.2790850449166963},{"site":"Trip(PL)","w1_rn":0,"w1_rev":0.0,"w1_adr":0,"w2_rn":1,"w2_rev":195.18,"w2_adr":195.18,"wow_rn":null,"wow_rev":null,"wow_adr":null},{"site":"Trip(SG)","w1_rn":13,"w1_rev":13854.7,"w1_adr":1065.75,"w2_rn":27,"w2_rev":19682.91,"w2_adr":729.0,"wow_rn":1.0769230769230769,"wow_rev":0.420666753520466,"wow_adr":-0.3159752668234793},{"site":"Trip(TH)","w1_rn":15,"w1_rev":7116.3,"w1_adr":474.42,"w2_rn":1,"w2_rev":673.5,"w2_adr":673.5,"wow_rn":-0.9333333333333333,"wow_rev":-0.9053581214957211,"wow_adr":0.4196281775641836},{"site":"Trip(TW)","w1_rn":998,"w1_rev":683483.83,"w1_adr":684.85,"w2_rn":1105,"w2_rev":777891.25,"w2_adr":703.97,"wow_rn":0.10721442885771543,"wow_rev":0.1381267667819163,"wow_adr":0.027919016514346164},{"site":"Trip(US)","w1_rn":4,"w1_rev":1058.66,"w1_adr":264.66,"w2_rn":7,"w2_rev":3335.78,"w2_adr":476.54,"wow_rn":0.75,"wow_rev":2.1509455349215045,"wow_adr":0.8005403056694312},{"site":"Trip(VN)","w1_rn":2,"w1_rev":615.0,"w1_adr":307.5,"w2_rn":0,"w2_rev":0.0,"w2_adr":0,"wow_rn":-1.0,"wow_rev":-1.0,"wow_adr":-1.0},{"site":"Trip(XX)","w1_rn":16,"w1_rev":11997.12,"w1_adr":749.82,"w2_rn":8,"w2_rev":5962.28,"w2_adr":745.28,"wow_rn":-0.5,"wow_rev":-0.5030240591075191,"wow_adr":-0.006048118215038234}],"total_w1_rn":2543,"total_w2_rn":2775},"台南":{"sites":[{"site":"Trip(AT)","w1_rn":1,"w1_rev":1160.68,"w1_adr":1160.68,"w2_rn":0,"w2_rev":0.0,"w2_adr":0,"wow_rn":-1.0,"wow_rev":-1.0,"wow_adr":-1.0},{"site":"Trip(AU)","w1_rn":16,"w1_rev":14715.01,"w1_adr":919.69,"w2_rn":10,"w2_rev":6898.84,"w2_adr":689.88,"wow_rn":-0.375,"wow_rev":-0.5311698734829267,"wow_adr":-0.24987179757268257},{"site":"Trip(BR)","w1_rn":0,"w1_rev":0.0,"w1_adr":0,"w2_rn":2,"w2_rev":1782.08,"w2_adr":891.04,"wow_rn":null,"wow_rev":null,"wow_adr":null},{"site":"Trip(CA)","w1_rn":17,"w1_rev":6355.94,"w1_adr":373.88,"w2_rn":1,"w2_rev":458.12,"w2_adr":458.12,"wow_rn":-0.9411764705882353,"wow_rev":-0.9279225417483488,"wow_adr":0.2253167902780706},{"site":"Trip(CH)","w1_rn":2,"w1_rev":1265.51,"w1_adr":632.75,"w2_rn":2,"w2_rev":573.34,"w2_adr":286.67,"wow_rn":0.0,"wow_rev":-0.5469494512093939,"wow_adr":-0.5469494512093939},{"site":"Trip(CN1)","w1_rn":1656,"w1_rev":1102386.48,"w1_adr":665.69,"w2_rn":2141,"w2_rev":1468419.94,"w2_adr":685.86,"wow_rn":0.2928743961352657,"wow_rev":0.33203732675204134,"wow_adr":0.030291365297235095},{"site":"Trip(DE)","w1_rn":1,"w1_rev":231.36,"w1_adr":231.36,"w2_rn":1,"w2_rev":696.59,"w2_adr":696.59,"wow_rn":0.0,"wow_rev":2.0108488934993085,"wow_adr":2.0108488934993085},{"site":"Trip(ES)","w1_rn":1,"w1_rev":587.85,"w1_adr":587.85,"w2_rn":1,"w2_rev":436.6,"w2_adr":436.6,"wow_rn":0.0,"wow_rev":-0.25729352726035554,"wow_adr":-0.25729352726035554},{"site":"Trip(FR)","w1_rn":14,"w1_rev":5053.14,"w1_adr":360.94,"w2_rn":9,"w2_rev":5598.43,"w2_adr":622.05,"wow_rn":-0.35714285714285715,"wow_rev":0.10791112061015526,"wow_adr":0.7234172987269083},{"site":"Trip(GB)","w1_rn":13,"w1_rev":8961.52,"w1_adr":689.35,"w2_rn":15,"w2_rev":5916.13,"w2_adr":394.41,"wow_rn":0.15384615384615385,"wow_rev":-0.3398296271168284,"wow_adr":-0.42785234350125134},{"site":"Trip(HK)","w1_rn":545,"w1_rev":326102.9,"w1_adr":598.35,"w2_rn":476,"w2_rev":311418.61,"w2_adr":654.24,"wow_rn":-0.12660550458715597,"wow_rev":-0.04502961955418057,"wow_adr":0.09340096080456216},{"site":"Trip(ID)","w1_rn":11,"w1_rev":3810.3,"w1_adr":346.39,"w2_rn":6,"w2_rev":4046.87,"w2_adr":674.48,"wow_rn":-0.45454545454545453,"wow_rev":0.06208697477888872,"wow_adr":0.947159453761296},{"site":"Trip(IL)","w1_rn":1,"w1_rev":335.78,"w1_adr":335.78,"w2_rn":3,"w2_rev":1728.81,"w2_adr":576.27,"wow_rn":2.0,"wow_rev":4.14863898981476,"wow_adr":0.71621299660492},{"site":"Trip(IT)","w1_rn":0,"w1_rev":0.0,"w1_adr":0,"w2_rn":6,"w2_rev":1608.29,"w2_adr":268.05,"wow_rn":null,"wow_rev":null,"wow_adr":null},{"site":"Trip(JP)","w1_rn":223,"w1_rev":131636.18,"w1_adr":590.3,"w2_rn":360,"w2_rev":188837.25,"w2_adr":524.55,"wow_rn":0.6143497757847534,"wow_rev":0.43453912138744866,"wow_adr":-0.11138271091833044},{"site":"Trip(KR)","w1_rn":152,"w1_rev":52208.08,"w1_adr":343.47,"w2_rn":111,"w2_rev":34820.18,"w2_adr":313.7,"wow_rn":-0.26973684210526316,"wow_rev":-0.33304998000309516,"wow_adr":-0.08669907171595004},{"site":"Trip(MY)","w1_rn":80,"w1_rev":48474.62,"w1_adr":605.93,"w2_rn":90,"w2_rev":57714.68,"w2_adr":641.27,"wow_rn":0.125,"wow_rev":0.19061645042292263,"wow_adr":0.05832573370926456},{"site":"Trip(NL)","w1_rn":2,"w1_rev":3137.33,"w1_adr":1568.66,"w2_rn":0,"w2_rev":0.0,"w2_adr":0,"wow_rn":-1.0,"wow_rev":-1.0,"wow_adr":-1.0},{"site":"Trip(NZ)","w1_rn":2,"w1_rev":698.71,"w1_adr":349.36,"w2_rn":0,"w2_rev":0.0,"w2_adr":0,"wow_rn":-1.0,"wow_rev":-1.0,"wow_adr":-1.0},{"site":"Trip(PH)","w1_rn":25,"w1_rev":9942.26,"w1_adr":397.69,"w2_rn":10,"w2_rev":4608.45,"w2_adr":460.84,"wow_rn":-0.6,"wow_rev":-0.5364793093871258,"wow_adr":0.15880172653218524},{"site":"Trip(RU)","w1_rn":5,"w1_rev":2368.52,"w1_adr":473.7,"w2_rn":0,"w2_rev":0.0,"w2_adr":0,"wow_rn":-1.0,"wow_rev":-1.0,"wow_adr":-1.0},{"site":"Trip(SG)","w1_rn":100,"w1_rev":58155.98,"w1_adr":581.56,"w2_rn":133,"w2_rev":109546.61,"w2_adr":823.66,"wow_rn":0.33,"wow_rev":0.8836688849538776,"wow_adr":0.4162923947021636},{"site":"Trip(TH)","w1_rn":35,"w1_rev":12469.41,"w1_adr":356.27,"w2_rn":28,"w2_rev":13948.03,"w2_adr":498.14,"wow_rn":-0.2,"wow_rev":0.11857978845831525,"wow_adr":0.39822473557289406},{"site":"Trip(TW)","w1_rn":1979,"w1_rev":1317671.76,"w1_adr":665.83,"w2_rn":2124,"w2_rev":1342355.69,"w2_adr":631.99,"wow_rn":0.07326932794340577,"wow_rev":0.018732991494831288,"wow_adr":-0.05081328146503248},{"site":"Trip(US)","w1_rn":67,"w1_rev":45384.93,"w1_adr":677.39,"w2_rn":42,"w2_rev":28357.25,"w2_adr":675.17,"wow_rn":-0.373134328358209,"wow_rev":-0.3751835631359007,"wow_adr":-0.003269017383460561},{"site":"Trip(VN)","w1_rn":12,"w1_rev":5519.24,"w1_adr":459.94,"w2_rn":9,"w2_rev":3436.65,"w2_adr":381.85,"wow_rn":-0.25,"wow_rev":-0.3773326697394693,"wow_adr":-0.16977689298595894},{"site":"Trip(XX)","w1_rn":80,"w1_rev":40389.65,"w1_adr":504.87,"w2_rn":49,"w2_rev":28107.47,"w2_adr":573.62,"wow_rn":-0.3875,"wow_rev":-0.30409226126000105,"wow_adr":0.13617589998367172}],"total_w1_rn":5040,"total_w2_rn":5629},"花蓮":{"sites":[{"site":"Trip(AE)","w1_rn":1,"w1_rev":611.89,"w1_adr":611.89,"w2_rn":0,"w2_rev":0.0,"w2_adr":0,"wow_rn":-1.0,"wow_rev":-1.0,"wow_adr":-1.0},{"site":"Trip(AU)","w1_rn":20,"w1_rev":8073.91,"w1_adr":403.7,"w2_rn":8,"w2_rev":2166.5,"w2_adr":270.81,"wow_rn":-0.6,"wow_rev":-0.7316665655178222,"wow_adr":-0.3291664137945555},{"site":"Trip(CA)","w1_rn":5,"w1_rev":2557.14,"w1_adr":511.43,"w2_rn":1,"w2_rev":370.41,"w2_adr":370.41,"wow_rn":-0.8,"wow_rev":-0.8551467655271124,"wow_adr":-0.27573382763556165},{"site":"Trip(CN1)","w1_rn":981,"w1_rev":655968.63,"w1_adr":668.67,"w2_rn":1238,"w2_rev":886147.03,"w2_adr":715.79,"wow_rn":0.2619775739041794,"wow_rev":0.35089849352233565,"wow_adr":0.0704615687765841},{"site":"Trip(DE)","w1_rn":3,"w1_rev":859.65,"w1_adr":286.55,"w2_rn":4,"w2_rev":1510.48,"w2_adr":377.62,"wow_rn":0.3333333333333333,"wow_rev":0.7570871866457279,"wow_adr":0.31781538998429587},{"site":"Trip(FR)","w1_rn":1,"w1_rev":645.53,"w1_adr":645.53,"w2_rn":5,"w2_rev":1339.67,"w2_adr":267.93,"wow_rn":4.0,"wow_rev":1.0753024646414575,"wow_adr":-0.5849395070717085},{"site":"Trip(GB)","w1_rn":11,"w1_rev":3847.66,"w1_adr":349.79,"w2_rn":6,"w2_rev":2303.82,"w2_adr":383.97,"wow_rn":-0.45454545454545453,"wow_rev":-0.4012412739171341,"wow_adr":0.09772433115192093},{"site":"Trip(HK)","w1_rn":121,"w1_rev":61613.86,"w1_adr":509.21,"w2_rn":138,"w2_rev":85184.25,"w2_adr":617.28,"wow_rn":0.14049586776859505,"wow_rev":0.3825501144270048,"wow_adr":0.21223596989614188},{"site":"Trip(ID)","w1_rn":20,"w1_rev":9938.65,"w1_adr":496.93,"w2_rn":0,"w2_rev":0.0,"w2_adr":0,"wow_rn":-1.0,"wow_rev":-1.0,"wow_adr":-1.0},{"site":"Trip(IL)","w1_rn":5,"w1_rev":1695.47,"w1_adr":339.09,"w2_rn":2,"w2_rev":471.98,"w2_adr":235.99,"wow_rn":-0.6,"wow_rev":-0.7216229128206337,"wow_adr":-0.3040572820515844},{"site":"Trip(JP)","w1_rn":36,"w1_rev":10968.88,"w1_adr":304.69,"w2_rn":20,"w2_rev":8540.06,"w2_adr":427.0,"wow_rn":-0.4444444444444444,"wow_rev":-0.22142828014998053,"wow_adr":0.40142909573003516},{"site":"Trip(KR)","w1_rn":0,"w1_rev":0.0,"w1_adr":0,"w2_rn":3,"w2_rev":1505.07,"w2_adr":501.69,"wow_rn":null,"wow_rev":null,"wow_adr":null},{"site":"Trip(MY)","w1_rn":16,"w1_rev":6123.88,"w1_adr":382.74,"w2_rn":34,"w2_rev":14063.61,"w2_adr":413.64,"wow_rn":1.125,"wow_rev":1.2965195268359273,"wow_adr":0.08071507145220115},{"site":"Trip(NZ)","w1_rn":0,"w1_rev":0.0,"w1_adr":0,"w2_rn":1,"w2_rev":875.54,"w2_adr":875.54,"wow_rn":null,"wow_rev":null,"wow_adr":null},{"site":"Trip(PH)","w1_rn":2,"w1_rev":1198.37,"w1_adr":599.18,"w2_rn":0,"w2_rev":0.0,"w2_adr":0,"wow_rn":-1.0,"wow_rev":-1.0,"wow_adr":-1.0},{"site":"Trip(SG)","w1_rn":16,"w1_rev":7433.79,"w1_adr":464.61,"w2_rn":26,"w2_rev":14869.97,"w2_adr":571.92,"wow_rn":0.625,"wow_rev":1.0003215049120298,"wow_adr":0.23096707994586435},{"site":"Trip(TH)","w1_rn":3,"w1_rev":1385.04,"w1_adr":461.68,"w2_rn":5,"w2_rev":1348.05,"w2_adr":269.61,"wow_rn":0.6666666666666666,"wow_rev":-0.02670680991162711,"wow_adr":-0.41602408594697626},{"site":"Trip(TW)","w1_rn":798,"w1_rev":543479.44,"w1_adr":681.05,"w2_rn":938,"w2_rev":688192.8,"w2_adr":733.68,"wow_rn":0.17543859649122806,"wow_rev":0.2662720043750765,"wow_adr":0.0772761828265576},{"site":"Trip(US)","w1_rn":12,"w1_rev":21387.02,"w1_adr":1782.25,"w2_rn":56,"w2_rev":35902.34,"w2_adr":641.11,"wow_rn":3.6666666666666665,"wow_rev":0.6786976399704121,"wow_adr":-0.6402790771491974},{"site":"Trip(VN)","w1_rn":2,"w1_rev":1777.86,"w1_adr":888.93,"w2_rn":13,"w2_rev":3607.03,"w2_adr":277.46,"wow_rn":5.5,"wow_rev":1.0288605402000162,"wow_adr":-0.6878676091999975},{"site":"Trip(XX)","w1_rn":19,"w1_rev":10990.26,"w1_adr":578.43,"w2_rn":26,"w2_rev":11390.2,"w2_adr":438.08,"wow_rn":0.3684210526315789,"wow_rev":0.036390403866696557,"wow_adr":-0.24263778178972176}],"total_w1_rn":2072,"total_w2_rn":2524},"金門":{"sites":[{"site":"Trip(CA)","w1_rn":2,"w1_rev":1442.88,"w1_adr":721.44,"w2_rn":0,"w2_rev":0.0,"w2_adr":0,"wow_rn":-1.0,"wow_rev":-1.0,"wow_adr":-1.0},{"site":"Trip(CN1)","w1_rn":354,"w1_rev":204435.88,"w1_adr":577.5,"w2_rn":264,"w2_rev":147521.61,"w2_adr":558.79,"wow_rn":-0.2542372881355932,"wow_rev":-0.2783966789211398,"wow_adr":-0.03239554673516469},{"site":"Trip(GB)","w1_rn":2,"w1_rev":1477.93,"w1_adr":738.96,"w2_rn":0,"w2_rev":0.0,"w2_adr":0,"wow_rn":-1.0,"wow_rev":-1.0,"wow_adr":-1.0},{"site":"Trip(HK)","w1_rn":27,"w1_rev":15900.21,"w1_adr":588.9,"w2_rn":11,"w2_rev":5500.62,"w2_adr":500.06,"wow_rn":-0.5925925925925926,"wow_rev":-0.6540536257068302,"wow_adr":-0.15085889946221967},{"site":"Trip(JP)","w1_rn":0,"w1_rev":0.0,"w1_adr":0,"w2_rn":4,"w2_rev":2109.59,"w2_adr":527.4,"wow_rn":null,"wow_rev":null,"wow_adr":null},{"site":"Trip(KR)","w1_rn":2,"w1_rev":993.32,"w1_adr":496.66,"w2_rn":0,"w2_rev":0.0,"w2_adr":0,"wow_rn":-1.0,"wow_rev":-1.0,"wow_adr":-1.0},{"site":"Trip(TW)","w1_rn":81,"w1_rev":43872.79,"w1_adr":541.64,"w2_rn":98,"w2_rev":55832.82,"w2_adr":569.72,"wow_rn":0.20987654320987653,"wow_rev":0.2726070076692184,"wow_adr":0.051848649195986564},{"site":"Trip(US)","w1_rn":2,"w1_rev":1198.88,"w1_adr":599.44,"w2_rn":0,"w2_rev":0.0,"w2_adr":0,"wow_rn":-1.0,"wow_rev":-1.0,"wow_adr":-1.0},{"site":"Trip(XX)","w1_rn":2,"w1_rev":676.56,"w1_adr":338.28,"w2_rn":0,"w2_rev":0.0,"w2_adr":0,"wow_rn":-1.0,"wow_rev":-1.0,"wow_adr":-1.0}],"total_w1_rn":472,"total_w2_rn":377},"南投":{"sites":[{"site":"Trip(AU)","w1_rn":8,"w1_rev":10027.6,"w1_adr":1253.45,"w2_rn":6,"w2_rev":4358.92,"w2_adr":726.49,"wow_rn":-0.25,"wow_rev":-0.5653077506083211,"wow_adr":-0.4204103341444281},{"site":"Trip(CA)","w1_rn":3,"w1_rev":5376.1,"w1_adr":1792.03,"w2_rn":0,"w2_rev":0.0,"w2_adr":0,"wow_rn":-1.0,"wow_rev":-1.0,"wow_adr":-1.0},{"site":"Trip(CN1)","w1_rn":490,"w1_rev":622679.0,"w1_adr":1270.77,"w2_rn":656,"w2_rev":860922.38,"w2_adr":1312.38,"wow_rn":0.33877551020408164,"wow_rev":0.3826102694968032,"wow_adr":0.032742426910721885},{"site":"Trip(DE)","w1_rn":5,"w1_rev":3534.1,"w1_adr":706.82,"w2_rn":0,"w2_rev":0.0,"w2_adr":0,"wow_rn":-1.0,"wow_rev":-1.0,"wow_adr":-1.0},{"site":"Trip(DK)","w1_rn":2,"w1_rev":2515.22,"w1_adr":1257.61,"w2_rn":1,"w2_rev":1226.34,"w2_adr":1226.34,"wow_rn":-0.5,"wow_rev":-0.5124323120840324,"wow_adr":-0.02486462416806481},{"site":"Trip(FR)","w1_rn":2,"w1_rev":2911.76,"w1_adr":1455.88,"w2_rn":4,"w2_rev":3339.36,"w2_adr":834.84,"wow_rn":1.0,"wow_rev":0.14685276259032334,"wow_adr":-0.42657361870483834},{"site":"Trip(HK)","w1_rn":80,"w1_rev":86509.69,"w1_adr":1081.37,"w2_rn":79,"w2_rev":85727.74,"w2_adr":1085.16,"wow_rn":-0.0125,"wow_rev":-0.009038871830427453,"wow_adr":0.003504939918554491},{"site":"Trip(ID)","w1_rn":3,"w1_rev":1702.3,"w1_adr":567.43,"w2_rn":9,"w2_rev":9941.83,"w2_adr":1104.65,"wow_rn":2.0,"wow_rev":4.840233801327616,"wow_adr":0.9467446004425386},{"site":"Trip(IL)","w1_rn":2,"w1_rev":1318.3,"w1_adr":659.15,"w2_rn":0,"w2_rev":0.0,"w2_adr":0,"wow_rn":-1.0,"wow_rev":-1.0,"wow_adr":-1.0},{"site":"Trip(IN)","w1_rn":1,"w1_rev":506.19,"w1_adr":506.19,"w2_rn":0,"w2_rev":0.0,"w2_adr":0,"wow_rn":-1.0,"wow_rev":-1.0,"wow_adr":-1.0},{"site":"Trip(JP)","w1_rn":6,"w1_rev":7601.46,"w1_adr":1266.91,"w2_rn":16,"w2_rev":13411.71,"w2_adr":838.23,"wow_rn":1.6666666666666667,"wow_rev":0.7643597414180964,"wow_adr":-0.3383650969682139},{"site":"Trip(KR)","w1_rn":0,"w1_rev":0.0,"w1_adr":0,"w2_rn":3,"w2_rev":2966.82,"w2_adr":988.94,"wow_rn":null,"wow_rev":null,"wow_adr":null},{"site":"Trip(MY)","w1_rn":27,"w1_rev":16146.42,"w1_adr":598.02,"w2_rn":25,"w2_rev":18629.68,"w2_adr":745.19,"wow_rn":-0.07407407407407407,"wow_rev":0.1537963214136631,"wow_adr":0.24610002712675616},{"site":"Trip(NL)","w1_rn":2,"w1_rev":1458.86,"w1_adr":729.43,"w2_rn":0,"w2_rev":0.0,"w2_adr":0,"wow_rn":-1.0,"wow_rev":-1.0,"wow_adr":-1.0},{"site":"Trip(NZ)","w1_rn":1,"w1_rev":367.55,"w1_adr":367.55,"w2_rn":0,"w2_rev":0.0,"w2_adr":0,"wow_rn":-1.0,"wow_rev":-1.0,"wow_adr":-1.0},{"site":"Trip(PH)","w1_rn":1,"w1_rev":454.37,"w1_adr":454.37,"w2_rn":1,"w2_rev":1552.43,"w2_adr":1552.43,"wow_rn":0.0,"wow_rev":2.4166648326253934,"wow_adr":2.4166648326253934},{"site":"Trip(RU)","w1_rn":2,"w1_rev":1719.24,"w1_adr":859.62,"w2_rn":0,"w2_rev":0.0,"w2_adr":0,"wow_rn":-1.0,"wow_rev":-1.0,"wow_adr":-1.0},{"site":"Trip(SG)","w1_rn":35,"w1_rev":29154.43,"w1_adr":832.98,"w2_rn":34,"w2_rev":37405.64,"w2_adr":1100.17,"wow_rn":-0.02857142857142857,"wow_rev":0.2830173664859853,"wow_adr":0.320753171382632},{"site":"Trip(TH)","w1_rn":14,"w1_rev":12262.18,"w1_adr":875.87,"w2_rn":37,"w2_rev":18294.34,"w2_adr":494.44,"wow_rn":1.6428571428571428,"wow_rev":0.4919321034269599,"wow_adr":-0.4354851500546638},{"site":"Trip(TW)","w1_rn":614,"w1_rev":661765.41,"w1_adr":1077.79,"w2_rn":703,"w2_rev":700600.06,"w2_adr":996.59,"wow_rn":0.1449511400651466,"wow_rev":0.05868339933927607,"wow_adr":-0.07534622020723254},{"site":"Trip(US)","w1_rn":7,"w1_rev":7119.63,"w1_adr":1017.09,"w2_rn":10,"w2_rev":10328.5,"w2_adr":1032.85,"wow_rn":0.42857142857142855,"wow_rev":0.45070741035699885,"wow_adr":0.0154951872498991},{"site":"Trip(VN)","w1_rn":1,"w1_rev":459.65,"w1_adr":459.65,"w2_rn":4,"w2_rev":2707.47,"w2_adr":676.87,"wow_rn":3.0,"wow_rev":4.890286087240292,"wow_adr":0.4725715218100731},{"site":"Trip(XX)","w1_rn":10,"w1_rev":8777.74,"w1_adr":877.77,"w2_rn":9,"w2_rev":9874.46,"w2_adr":1097.16,"wow_rn":-0.1,"wow_rev":0.12494332254088175,"wow_adr":0.24993702504542425}],"total_w1_rn":1316,"total_w2_rn":1597},"屏東":{"sites":[{"site":"Trip(BY)","w1_rn":0,"w1_rev":0.0,"w1_adr":0,"w2_rn":4,"w2_rev":4429.61,"w2_adr":1107.4,"wow_rn":null,"wow_rev":null,"wow_adr":null},{"site":"Trip(CA)","w1_rn":8,"w1_rev":7527.7,"w1_adr":940.96,"w2_rn":1,"w2_rev":338.34,"w2_adr":338.34,"wow_rn":-0.875,"wow_rev":-0.9550540005579393,"wow_adr":-0.6404320044635147},{"site":"Trip(CH)","w1_rn":4,"w1_rev":8966.04,"w1_adr":2241.51,"w2_rn":0,"w2_rev":0.0,"w2_adr":0,"wow_rn":-1.0,"wow_rev":-1.0,"wow_adr":-1.0},{"site":"Trip(CN1)","w1_rn":523,"w1_rev":740530.29,"w1_adr":1415.93,"w2_rn":462,"w2_rev":672920.68,"w2_adr":1456.54,"wow_rn":-0.11663479923518165,"wow_rev":-0.09129891190423782,"wow_adr":0.028681101891955912},{"site":"Trip(FR)","w1_rn":3,"w1_rev":3643.21,"w1_adr":1214.4,"w2_rn":0,"w2_rev":0.0,"w2_adr":0,"wow_rn":-1.0,"wow_rev":-1.0,"wow_adr":-1.0},{"site":"Trip(GB)","w1_rn":0,"w1_rev":0.0,"w1_adr":0,"w2_rn":12,"w2_rev":10551.56,"w2_adr":879.3,"wow_rn":null,"wow_rev":null,"wow_adr":null},{"site":"Trip(HK)","w1_rn":89,"w1_rev":91002.15,"w1_adr":1022.5,"w2_rn":129,"w2_rev":165193.38,"w2_adr":1280.57,"wow_rn":0.449438202247191,"wow_rev":0.8152690238637212,"wow_adr":0.25239490793698593},{"site":"Trip(JP)","w1_rn":6,"w1_rev":5330.44,"w1_adr":888.41,"w2_rn":12,"w2_rev":13922.12,"w2_adr":1160.18,"wow_rn":1.0,"wow_rev":1.6118144093170548,"wow_adr":0.3059072046585271},{"site":"Trip(KR)","w1_rn":14,"w1_rev":19109.95,"w1_adr":1365.0,"w2_rn":15,"w2_rev":22540.77,"w2_adr":1502.72,"wow_rn":0.07142857142857142,"wow_rev":0.1795305586880133,"wow_adr":0.10089518810881244},{"site":"Trip(MY)","w1_rn":0,"w1_rev":0.0,"w1_adr":0,"w2_rn":2,"w2_rev":1404.31,"w2_adr":702.15,"wow_rn":null,"wow_rev":null,"wow_adr":null},{"site":"Trip(PH)","w1_rn":1,"w1_rev":508.06,"w1_adr":508.06,"w2_rn":0,"w2_rev":0.0,"w2_adr":0,"wow_rn":-1.0,"wow_rev":-1.0,"wow_adr":-1.0},{"site":"Trip(RU)","w1_rn":5,"w1_rev":5939.96,"w1_adr":1187.99,"w2_rn":0,"w2_rev":0.0,"w2_adr":0,"wow_rn":-1.0,"wow_rev":-1.0,"wow_adr":-1.0},{"site":"Trip(SG)","w1_rn":10,"w1_rev":14116.56,"w1_adr":1411.66,"w2_rn":0,"w2_rev":0.0,"w2_adr":0,"wow_rn":-1.0,"wow_rev":-1.0,"wow_adr":-1.0},{"site":"Trip(TH)","w1_rn":4,"w1_rev":2679.4,"w1_adr":669.85,"w2_rn":2,"w2_rev":1649.42,"w2_adr":824.71,"wow_rn":-0.5,"wow_rev":-0.38440695678136894,"wow_adr":0.23118608643726207},{"site":"Trip(TW)","w1_rn":456,"w1_rev":516131.23,"w1_adr":1131.87,"w2_rn":457,"w2_rev":600051.29,"w2_adr":1313.02,"wow_rn":0.0021929824561403508,"wow_rev":0.1625944089903019,"wow_adr":0.16005043872992933},{"site":"Trip(US)","w1_rn":8,"w1_rev":23957.7,"w1_adr":2994.71,"w2_rn":13,"w2_rev":12852.09,"w2_adr":988.62,"wow_rn":0.625,"wow_rev":-0.46355075821134745,"wow_adr":-0.6698773896685215},{"site":"Trip(VN)","w1_rn":3,"w1_rev":1562.39,"w1_adr":520.8,"w2_rn":8,"w2_rev":14695.86,"w2_adr":1836.98,"wow_rn":1.6666666666666667,"wow_rev":8.405994522504901,"wow_adr":2.5272479459393375},{"site":"Trip(XX)","w1_rn":36,"w1_rev":57416.99,"w1_adr":1594.92,"w2_rn":18,"w2_rev":16761.11,"w2_adr":931.17,"wow_rn":-0.5,"wow_rev":-0.7080810134259977,"wow_adr":-0.4161620268519954}],"total_w1_rn":1170,"total_w2_rn":1135},"高雄":{"sites":[{"site":"Trip(AU)","w1_rn":21,"w1_rev":18745.33,"w1_adr":892.63,"w2_rn":35,"w2_rev":14673.3,"w2_adr":419.24,"wow_rn":0.6666666666666666,"wow_rev":-0.21722903784569278,"wow_adr":-0.5303374227074157},{"site":"Trip(BR)","w1_rn":0,"w1_rev":0.0,"w1_adr":0,"w2_rn":4,"w2_rev":1965.15,"w2_adr":491.29,"wow_rn":null,"wow_rev":null,"wow_adr":null},{"site":"Trip(CA)","w1_rn":24,"w1_rev":12657.5,"w1_adr":527.4,"w2_rn":9,"w2_rev":6657.11,"w2_adr":739.68,"wow_rn":-0.625,"wow_rev":-0.47405806833892944,"wow_adr":0.4025118177628548},{"site":"Trip(CH)","w1_rn":5,"w1_rev":3346.57,"w1_adr":669.31,"w2_rn":0,"w2_rev":0.0,"w2_adr":0,"wow_rn":-1.0,"wow_rev":-1.0,"wow_adr":-1.0},{"site":"Trip(CN1)","w1_rn":3251,"w1_rev":2210320.84,"w1_adr":679.89,"w2_rn":3778,"w2_rev":2665243.97,"w2_adr":705.46,"wow_rn":0.1621039680098431,"wow_rev":0.20581769041355508,"wow_adr":0.03761601681695795},{"site":"Trip(DE)","w1_rn":30,"w1_rev":10278.28,"w1_adr":342.61,"w2_rn":14,"w2_rev":6394.51,"w2_adr":456.75,"wow_rn":-0.5333333333333333,"wow_rev":-0.37786186015559015,"wow_adr":0.33315315680944985},{"site":"Trip(ES)","w1_rn":15,"w1_rev":5779.04,"w1_adr":385.27,"w2_rn":3,"w2_rev":2284.98,"w2_adr":761.66,"wow_rn":-0.8,"wow_rev":-0.6046090700185498,"wow_adr":0.9769546499072506},{"site":"Trip(FI)","w1_rn":0,"w1_rev":0.0,"w1_adr":0,"w2_rn":4,"w2_rev":1151.16,"w2_adr":287.79,"wow_rn":null,"wow_rev":null,"wow_adr":null},{"site":"Trip(FR)","w1_rn":16,"w1_rev":7669.57,"w1_adr":479.35,"w2_rn":12,"w2_rev":4791.66,"w2_adr":399.31,"wow_rn":-0.25,"wow_rev":-0.37523746442108225,"wow_adr":-0.16698328589477632},{"site":"Trip(GB)","w1_rn":23,"w1_rev":10372.08,"w1_adr":450.96,"w2_rn":19,"w2_rev":17494.55,"w2_adr":920.77,"wow_rn":-0.17391304347826086,"wow_rev":0.6866959761205079,"wow_adr":1.0417898658300886},{"site":"Trip(HK)","w1_rn":2457,"w1_rev":1651393.52,"w1_adr":672.12,"w2_rn":2484,"w2_rev":1749307.91,"w2_adr":704.23,"wow_rn":0.01098901098901099,"wow_rev":0.059291980492711845,"wow_adr":0.047777937226486704},{"site":"Trip(ID)","w1_rn":49,"w1_rev":34139.94,"w1_adr":696.73,"w2_rn":25,"w2_rev":11119.48,"w2_adr":444.78,"wow_rn":-0.4897959183673469,"wow_rev":-0.6742970257124061,"wow_adr":-0.3616221703963159},{"site":"Trip(IL)","w1_rn":2,"w1_rev":438.54,"w1_adr":219.27,"w2_rn":1,"w2_rev":208.76,"w2_adr":208.76,"wow_rn":-0.5,"wow_rev":-0.5239658868062207,"wow_adr":-0.047931773612441365},{"site":"Trip(IN)","w1_rn":3,"w1_rev":947.13,"w1_adr":315.71,"w2_rn":1,"w2_rev":449.29,"w2_adr":449.29,"wow_rn":-0.6666666666666666,"wow_rev":-0.5256300613432159,"wow_adr":0.42310981597035247},{"site":"Trip(IT)","w1_rn":3,"w1_rev":5251.97,"w1_adr":1750.66,"w2_rn":0,"w2_rev":0.0,"w2_adr":0,"wow_rn":-1.0,"wow_rev":-1.0,"wow_adr":-1.0},{"site":"Trip(JP)","w1_rn":704,"w1_rev":546856.79,"w1_adr":776.79,"w2_rn":1106,"w2_rev":884971.3,"w2_adr":800.15,"wow_rn":0.5710227272727273,"wow_rev":0.6182871204726204,"wow_adr":0.030085111042246596},{"site":"Trip(KR)","w1_rn":316,"w1_rev":174446.44,"w1_adr":552.05,"w2_rn":205,"w2_rev":105697.86,"w2_adr":515.6,"wow_rn":-0.3512658227848101,"wow_rev":-0.3940956192628525,"wow_adr":-0.06602056432712894},{"site":"Trip(MY)","w1_rn":136,"w1_rev":71897.37,"w1_adr":528.66,"w2_rn":154,"w2_rev":99083.49,"w2_adr":643.4,"wow_rn":0.1323529411764706,"wow_rev":0.378123984229187,"wow_adr":0.21704455750110016},{"site":"Trip(NL)","w1_rn":11,"w1_rev":4419.74,"w1_adr":401.79,"w2_rn":2,"w2_rev":534.53,"w2_adr":267.26,"wow_rn":-0.8181818181818182,"wow_rev":-0.8790584966536493,"wow_adr":-0.33482173159507117},{"site":"Trip(NZ)","w1_rn":0,"w1_rev":0.0,"w1_adr":0,"w2_rn":1,"w2_rev":341.7,"w2_adr":341.7,"wow_rn":null,"wow_rev":null,"wow_adr":null},{"site":"Trip(PH)","w1_rn":79,"w1_rev":39725.87,"w1_adr":502.86,"w2_rn":130,"w2_rev":81670.77,"w2_adr":628.24,"wow_rn":0.6455696202531646,"wow_rev":1.0558586205915694,"wow_adr":0.24932946943641524},{"site":"Trip(RU)","w1_rn":2,"w1_rev":320.2,"w1_adr":160.1,"w2_rn":14,"w2_rev":7944.62,"w2_adr":567.47,"wow_rn":6.0,"wow_rev":23.811430356027483,"wow_adr":2.544490050861069},{"site":"Trip(SE)","w1_rn":0,"w1_rev":0.0,"w1_adr":0,"w2_rn":3,"w2_rev":1012.71,"w2_adr":337.57,"wow_rn":null,"wow_rev":null,"wow_adr":null},{"site":"Trip(SG)","w1_rn":204,"w1_rev":142099.46,"w1_adr":696.57,"w2_rn":261,"w2_rev":209313.19,"w2_adr":801.97,"wow_rn":0.27941176470588236,"wow_rev":0.47300480310185955,"wow_adr":0.15131409897616596},{"site":"Trip(TH)","w1_rn":132,"w1_rev":63333.25,"w1_adr":479.8,"w2_rn":163,"w2_rev":81646.86,"w2_adr":500.9,"wow_rn":0.23484848484848486,"wow_rev":0.2891626534128735,"wow_adr":0.04398448006441282},{"site":"Trip(TW)","w1_rn":3296,"w1_rev":1927149.42,"w1_adr":584.69,"w2_rn":3126,"w2_rev":1966460.37,"w2_adr":629.07,"wow_rn":-0.05157766990291262,"wow_rev":0.020398495921313094,"wow_adr":0.07589041668478806},{"site":"Trip(US)","w1_rn":74,"w1_rev":43724.78,"w1_adr":590.88,"w2_rn":80,"w2_rev":52616.01,"w2_adr":657.7,"wow_rn":0.08108108108108109,"wow_rev":0.2033453341560553,"wow_adr":0.11309443409435112},{"site":"Trip(VN)","w1_rn":37,"w1_rev":14219.58,"w1_adr":384.31,"w2_rn":19,"w2_rev":10618.21,"w2_adr":558.85,"wow_rn":-0.4864864864864865,"wow_rev":-0.2532685393795589,"wow_adr":0.4541612654187537},{"site":"Trip(XX)","w1_rn":144,"w1_rev":84363.6,"w1_adr":585.86,"w2_rn":168,"w2_rev":128521.65,"w2_adr":765.01,"wow_rn":0.16666666666666666,"wow_rev":0.5234253872523221,"wow_adr":0.30579318907341907}],"total_w1_rn":11034,"total_w2_rn":11821},"嘉義":{"sites":[{"site":"Trip(AU)","w1_rn":4,"w1_rev":1654.35,"w1_adr":413.59,"w2_rn":3,"w2_rev":2037.76,"w2_adr":679.25,"wow_rn":-0.25,"wow_rev":0.2317586967691239,"wow_adr":0.6423449290254986},{"site":"Trip(BR)","w1_rn":0,"w1_rev":0.0,"w1_adr":0,"w2_rn":2,"w2_rev":1067.12,"w2_adr":533.56,"wow_rn":null,"wow_rev":null,"wow_adr":null},{"site":"Trip(CA)","w1_rn":6,"w1_rev":8598.49,"w1_adr":1433.08,"w2_rn":4,"w2_rev":2035.97,"w2_adr":508.99,"wow_rn":-0.3333333333333333,"wow_rev":-0.7632177277638283,"wow_adr":-0.6448265916457425},{"site":"Trip(CN1)","w1_rn":883,"w1_rev":613417.22,"w1_adr":694.7,"w2_rn":750,"w2_rev":548417.1,"w2_adr":731.22,"wow_rn":-0.1506228765571914,"wow_rev":-0.10596395234048041,"wow_adr":0.052578440111140975},{"site":"Trip(DE)","w1_rn":2,"w1_rev":450.72,"w1_adr":225.36,"w2_rn":0,"w2_rev":0.0,"w2_adr":0,"wow_rn":-1.0,"wow_rev":-1.0,"wow_adr":-1.0},{"site":"Trip(ES)","w1_rn":1,"w1_rev":242.4,"w1_adr":242.4,"w2_rn":1,"w2_rev":434.77,"w2_adr":434.77,"wow_rn":0.0,"wow_rev":0.7936056105610559,"wow_adr":0.7936056105610559},{"site":"Trip(FR)","w1_rn":1,"w1_rev":102.5,"w1_adr":102.5,"w2_rn":0,"w2_rev":0.0,"w2_adr":0,"wow_rn":-1.0,"wow_rev":-1.0,"wow_adr":-1.0},{"site":"Trip(GB)","w1_rn":2,"w1_rev":1971.34,"w1_adr":985.67,"w2_rn":2,"w2_rev":501.5,"w2_adr":250.75,"wow_rn":0.0,"wow_rev":-0.7456045126665111,"wow_adr":-0.7456045126665111},{"site":"Trip(HK)","w1_rn":93,"w1_rev":72086.72,"w1_adr":775.13,"w2_rn":132,"w2_rev":89277.26,"w2_adr":676.34,"wow_rn":0.41935483870967744,"wow_rev":0.23847027580114563,"wow_adr":-0.1274413965946474},{"site":"Trip(ID)","w1_rn":4,"w1_rev":1644.25,"w1_adr":411.06,"w2_rn":6,"w2_rev":1708.68,"w2_adr":284.78,"wow_rn":0.5,"wow_rev":0.039185038771476395,"wow_adr":-0.307209974152349},{"site":"Trip(IN)","w1_rn":2,"w1_rev":809.16,"w1_adr":404.58,"w2_rn":0,"w2_rev":0.0,"w2_adr":0,"wow_rn":-1.0,"wow_rev":-1.0,"wow_adr":-1.0},{"site":"Trip(JP)","w1_rn":14,"w1_rev":9399.73,"w1_adr":671.41,"w2_rn":17,"w2_rev":14258.17,"w2_adr":838.72,"wow_rn":0.21428571428571427,"wow_rev":0.5168701654196453,"wow_adr":0.2491871950514726},{"site":"Trip(KR)","w1_rn":3,"w1_rev":1087.07,"w1_adr":362.36,"w2_rn":1,"w2_rev":252.5,"w2_adr":252.5,"wow_rn":-0.6666666666666666,"wow_rev":-0.767724249588343,"wow_adr":-0.30317274876502887},{"site":"Trip(MY)","w1_rn":48,"w1_rev":23746.73,"w1_adr":494.72,"w2_rn":19,"w2_rev":10866.14,"w2_adr":571.9,"wow_rn":-0.6041666666666666,"wow_rev":-0.5424153136031782,"wow_adr":0.15600341826565525},{"site":"Trip(PH)","w1_rn":16,"w1_rev":7823.92,"w1_adr":488.99,"w2_rn":8,"w2_rev":2852.27,"w2_adr":356.53,"wow_rn":-0.5,"wow_rev":-0.6354423358112047,"wow_adr":-0.27088467162240915},{"site":"Trip(SG)","w1_rn":45,"w1_rev":44818.86,"w1_adr":995.97,"w2_rn":42,"w2_rev":22023.43,"w2_adr":524.37,"wow_rn":-0.06666666666666667,"wow_rev":-0.5086124457427075,"wow_adr":-0.47351333472432944},{"site":"Trip(TH)","w1_rn":6,"w1_rev":2471.67,"w1_adr":411.94,"w2_rn":7,"w2_rev":4124.39,"w2_adr":589.2,"wow_rn":0.16666666666666666,"wow_rev":0.668665315353587,"wow_adr":0.43028455601736015},{"site":"Trip(TW)","w1_rn":935,"w1_rev":618244.62,"w1_adr":661.22,"w2_rn":970,"w2_rev":663806.77,"w2_adr":684.34,"wow_rn":0.0374331550802139,"wow_rev":0.0736959957694421,"wow_adr":0.034954387674668366},{"site":"Trip(US)","w1_rn":9,"w1_rev":4838.4,"w1_adr":537.6,"w2_rn":13,"w2_rev":14356.61,"w2_adr":1104.35,"wow_rn":0.4444444444444444,"wow_rev":1.9672226355820108,"wow_adr":1.054231055402931},{"site":"Trip(VN)","w1_rn":2,"w1_rev":292.8,"w1_adr":146.4,"w2_rn":1,"w2_rev":834.32,"w2_adr":834.32,"wow_rn":-0.5,"wow_rev":1.849453551912569,"wow_adr":4.698907103825138},{"site":"Trip(XX)","w1_rn":20,"w1_rev":17656.92,"w1_adr":882.85,"w2_rn":7,"w2_rev":3226.7,"w2_adr":460.96,"wow_rn":-0.65,"wow_rev":-0.8172557841344923,"wow_adr":-0.4778736689556924}],"total_w1_rn":2096,"total_w2_rn":1985}},"ez_share":[{"mm":"Abby Cheng （鄭任妤）","total_w1":7133,"total_w2":7673,"wow_total":540,"maintenance":[{"type":"HPP","w1_rn":5896,"w2_rn":6415,"wow":519,"w1_pct":0.8265806813402495,"w2_pct":0.8360484816890394,"wow_pct":0.009467800348789912},{"type":"HTL","w1_rn":279,"w2_rn":287,"wow":8,"w1_pct":0.03911397728865835,"w2_pct":0.037403883748208,"wow_pct":-0.001710093540450347},{"type":"SHT","w1_rn":958,"w2_rn":971,"wow":13,"w1_pct":0.1343053413710921,"w2_pct":0.1265476345627525,"wow_pct":-0.007757706808339593}]},{"mm":"Hino Chi （籍喆）","total_w1":10539,"total_w2":10362,"wow_total":-177,"maintenance":[{"type":"HPP","w1_rn":9292,"w2_rn":9491,"wow":199,"w1_pct":0.881677578517886,"w2_pct":0.9159428681721675,"wow_pct":0.03426528965428155},{"type":"HTL","w1_rn":59,"w2_rn":63,"wow":4,"w1_pct":0.005598254103804915,"w2_pct":0.006079907353792704,"wow_pct":0.00048165324998778944},{"type":"SHT","w1_rn":1188,"w2_rn":808,"wow":-380,"w1_pct":0.11272416737830913,"w2_pct":0.07797722447403976,"wow_pct":-0.03474694290426937}]},{"mm":"Sandy Su （蘇筱鈞）","total_w1":8874,"total_w2":9564,"wow_total":690,"maintenance":[{"type":"HPP","w1_rn":6432,"w2_rn":7123,"wow":691,"w1_pct":0.7248140635564571,"w2_pct":0.7447720618987871,"wow_pct":0.01995799834233003},{"type":"HTL","w1_rn":335,"w2_rn":355,"wow":20,"w1_pct":0.03775073247689881,"w2_pct":0.03711836051861146,"wow_pct":-0.0006323719582873449},{"type":"SHT","w1_rn":2107,"w2_rn":2086,"wow":-21,"w1_pct":0.23743520396664414,"w2_pct":0.2181095775826014,"wow_pct":-0.019325626384042727}]},{"mm":"Wayne Wang （王俊明）","total_w1":2400,"total_w2":2411,"wow_total":11,"maintenance":[{"type":"HPP","w1_rn":1500,"w2_rn":1440,"wow":-60,"w1_pct":0.625,"w2_pct":0.5972625466611364,"wow_pct":-0.02773745333886357},{"type":"HTL","w1_rn":65,"w2_rn":92,"wow":27,"w1_pct":0.027083333333333334,"w2_pct":0.03815844048112816,"wow_pct":0.011075107147794826},{"type":"SHT","w1_rn":835,"w2_rn":879,"wow":44,"w1_pct":0.34791666666666665,"w2_pct":0.36457901285773536,"wow_pct":0.01666234619106871}]},{"mm":"Carol Lin （林芝榕）","total_w1":3830,"total_w2":4202,"wow_total":372,"maintenance":[{"type":"HPP","w1_rn":2832,"w2_rn":3141,"wow":309,"w1_pct":0.739425587467363,"w2_pct":0.7475011899095668,"wow_pct":0.008075602442203844},{"type":"HTL","w1_rn":141,"w2_rn":191,"wow":50,"w1_pct":0.03681462140992167,"w2_pct":0.045454545454545456,"wow_pct":0.008639924044623784},{"type":"SHT","w1_rn":857,"w2_rn":870,"wow":13,"w1_pct":0.2237597911227154,"w2_pct":0.20704426463588768,"wow_pct":-0.016715526486827725}]},{"mm":"Flora Tsao （曹芳綺）","total_w1":809,"total_w2":807,"wow_total":-2,"maintenance":[{"type":"HPP","w1_rn":684,"w2_rn":711,"wow":27,"w1_pct":0.8454882571075402,"w2_pct":0.8810408921933085,"wow_pct":0.035552635085768336},{"type":"HTL","w1_rn":0,"w2_rn":0,"wow":0,"w1_pct":0.0,"w2_pct":0.0,"wow_pct":0.0},{"type":"SHT","w1_rn":125,"w2_rn":96,"wow":-29,"w1_pct":0.15451174289245984,"w2_pct":0.11895910780669144,"wow_pct":-0.03555263508576839}]},{"mm":"Justin Lee （李岳勳）","total_w1":3522,"total_w2":4199,"wow_total":677,"maintenance":[{"type":"HPP","w1_rn":2941,"w2_rn":3491,"wow":550,"w1_pct":0.8350369108461102,"w2_pct":0.8313884258156704,"wow_pct":-0.0036484850304397964},{"type":"HTL","w1_rn":25,"w2_rn":20,"wow":-5,"w1_pct":0.007098239636570131,"w2_pct":0.004763038818766373,"wow_pct":-0.002335200817803758},{"type":"SHT","w1_rn":556,"w2_rn":688,"wow":132,"w1_pct":0.15786484951731972,"w2_pct":0.16384853536556324,"wow_pct":0.00598368584824352}]}]};

function n(v,t){
  if(v===null||v===undefined)return'<span class="wow-nt">—</span>';
  if(t==='rn')return'<span class="num-rn">'+Number(v).toLocaleString()+'</span>';
  if(t==='rev')return'<span class="num-rev">'+Number(v).toLocaleString('en-US',{maximumFractionDigits:0})+'</span>';
  if(t==='adr')return'<span class="num-adr">'+Number(v).toLocaleString('en-US',{minimumFractionDigits:0,maximumFractionDigits:0})+'</span>';
  return v;
}
function w(v){
  if(v===null||v===undefined)return'<span class="wow-nt">—</span>';
  const p=(v*100).toFixed(1),cls=v>=0?'wow-up':'wow-dn',s=v>=0?'+':'';
  return`<span class="${cls}">${s}${p}%</span>`;
}
function showSection(name,el){
  document.querySelectorAll('.section').forEach(s=>s.classList.remove('active'));
  document.querySelectorAll('.tab').forEach(t=>t.classList.remove('active'));
  document.getElementById('sec-'+name).classList.add('active');
  el.classList.add('active');
}

// Labels
['mm','city','site'].forEach(k=>{
  const a=document.getElementById('lbl-w1-'+k);
  const b=document.getElementById('lbl-w2-'+k);
  if(a)a.textContent=D.week1_label;
  if(b)b.textContent=D.week2_label;
});
document.getElementById('reportMeta').textContent='Book Day '+D.report_date;
document.getElementById('weekBadge').textContent=D.week1_label+' → '+D.week2_label;

// Summary
const tW1rn=D.mm_overview.reduce((s,m)=>s+m.w1_rn,0);
const tW2rn=D.mm_overview.reduce((s,m)=>s+m.w2_rn,0);
const tW1rev=D.mm_overview.reduce((s,m)=>s+m.w1_rev,0);
const tW2rev=D.mm_overview.reduce((s,m)=>s+m.w2_rev,0);
const wRn=(tW2rn-tW1rn)/tW1rn,wRev=(tW2rev-tW1rev)/tW1rev;
document.getElementById('mm-summary').innerHTML=[
  {l:D.week1_label+' RN',v:tW1rn.toLocaleString(),w:null},
  {l:D.week2_label+' RN',v:tW2rn.toLocaleString(),w:wRn},
  {l:D.week1_label+' REV (TWD)',v:(tW1rev/1e6).toFixed(2)+'M',w:null},
  {l:D.week2_label+' REV (TWD)',v:(tW2rev/1e6).toFixed(2)+'M',w:wRev},
].map(s=>`<div class="summary-card">
  <div class="summary-card-label">${s.l}</div>
  <div class="summary-card-value">${s.v}</div>
  ${s.w!==null?`<div class="summary-card-wow ${s.w>=0?'wow-up':'wow-dn'}">${s.w>=0?'+':''}${(s.w*100).toFixed(1)}% WoW</div>`:''}
</div>`).join('');

// MM table
let mmH='';
D.mm_overview.forEach(m=>{
  const fname=m.name.split(' ')[0];
  const cname=m.name.match(/（([^）]+)）/)?m.name.match(/（([^）]+)）/)[1]:'';
  mmH+=`<tr>
    <td><b>${fname}</b> <span style="color:var(--text3);font-size:11px">${cname}</span></td>
    <td>${n(m.w1_rn,'rn')}</td><td>${n(m.w1_rev,'rev')}</td><td>${n(m.w1_adr,'adr')}</td>
    <td>${n(m.w2_rn,'rn')}</td><td>${n(m.w2_rev,'rev')}</td><td>${n(m.w2_adr,'adr')}</td>
    <td>${w(m.wow_rn)}</td><td>${w(m.wow_rev)}</td><td>${w(m.wow_adr)}</td>
  </tr>`;
});
const tAdr1=tW1rev/tW1rn,tAdr2=tW2rev/tW2rn;
mmH+=`<tr class="row-total">
  <td>Others 總計</td>
  <td>${n(tW1rn,'rn')}</td><td>${n(tW1rev,'rev')}</td><td>${n(tAdr1,'adr')}</td>
  <td>${n(tW2rn,'rn')}</td><td>${n(tW2rev,'rev')}</td><td>${n(tAdr2,'adr')}</td>
  <td>${w(wRn)}</td><td>${w(wRev)}</td><td>${w((tAdr2-tAdr1)/tAdr1)}</td>
</tr>`;
document.getElementById('mm-tbody').innerHTML=mmH;

// City+Star table
let cH='';
D.city_star_overview.forEach(c=>{
  cH+=`<tr class="row-city">
    <td>${c.city}</td>
    <td>${n(c.w1_rn,'rn')}</td><td>${n(c.w1_rev,'rev')}</td><td>${n(c.w1_adr,'adr')}</td>
    <td>${n(c.w2_rn,'rn')}</td><td>${n(c.w2_rev,'rev')}</td><td>${n(c.w2_adr,'adr')}</td>
    <td>${w(c.wow_rn)}</td><td>${w(c.wow_rev)}</td><td>${w(c.wow_adr)}</td>
  </tr>`;
  c.stars.forEach(s=>{
    cH+=`<tr class="row-star">
      <td>${'★'.repeat(s.star)} ${s.star}星</td>
      <td>${n(s.w1_rn,'rn')}</td><td>${n(s.w1_rev,'rev')}</td><td>${n(s.w1_adr,'adr')}</td>
      <td>${n(s.w2_rn,'rn')}</td><td>${n(s.w2_rev,'rev')}</td><td>${n(s.w2_adr,'adr')}</td>
      <td>${w(s.wow_rn)}</td><td>${w(s.wow_rev)}</td><td>${w(s.wow_adr)}</td>
    </tr>`;
  });
});
document.getElementById('city-tbody').innerHTML=cH;

// Site by city
const cities=Object.keys(D.city_site_overview);
let selCity=cities[0];
function renderSite(city){
  const data=D.city_site_overview[city];
  const rows=data.sites.filter(s=>s.w1_rn>0||s.w2_rn>0).sort((a,b)=>b.w2_rn-a.w2_rn);
  let h='';
  rows.forEach(s=>{
    h+=`<tr>
      <td>${s.site}</td>
      <td>${n(s.w1_rn,'rn')}</td><td>${n(s.w1_rev,'rev')}</td><td>${n(s.w1_adr,'adr')}</td>
      <td>${n(s.w2_rn,'rn')}</td><td>${n(s.w2_rev,'rev')}</td><td>${n(s.w2_adr,'adr')}</td>
      <td>${w(s.wow_rn)}</td><td>${w(s.wow_rev)}</td><td>${w(s.wow_adr)}</td>
    </tr>`;
  });
  const wowTotal=(data.total_w2_rn-data.total_w1_rn)/data.total_w1_rn;
  h+=`<tr class="row-total">
    <td>Total</td>
    <td>${n(data.total_w1_rn,'rn')}</td><td>—</td><td>—</td>
    <td>${n(data.total_w2_rn,'rn')}</td><td>—</td><td>—</td>
    <td>${w(wowTotal)}</td><td>—</td><td>—</td>
  </tr>`;
  document.getElementById('site-tbody').innerHTML=h;
  document.querySelectorAll('.city-tab').forEach(t=>t.classList.toggle('active',t.dataset.city===city));
}
document.getElementById('site-city-tabs').innerHTML=cities.map(c=>
  `<div class="city-tab${c===selCity?' active':''}" data-city="${c}" onclick="selCity='${c}';renderSite('${c}')">${c}</div>`
).join('');
renderSite(selCity);

// EZ Share
let eH='';
D.ez_share.forEach(e=>{
  const fname=e.mm.split(' ')[0];
  const wSign=e.wow_total>=0?'+':'';
  const wCls=e.wow_total>=0?'wow-up':'wow-dn';
  eH+=`<div class="ez-card">
    <div class="ez-card-title">${fname}</div>
    <div class="ez-card-total">${e.total_w1.toLocaleString()} → ${e.total_w2.toLocaleString()} RN &nbsp;<span class="${wCls}">${wSign}${e.wow_total}</span></div>`;
  e.maintenance.forEach(m=>{
    const tc=m.type.toLowerCase();
    const p1=(m.w1_pct*100).toFixed(1),p2=(m.w2_pct*100).toFixed(1);
    const pwow=(m.wow_pct*100).toFixed(1);
    const pwCls=m.wow_pct>=0?'pct-up':'pct-dn';
    const pwSign=m.wow_pct>=0?'+':'';
    eH+=`<div class="ez-row">
      <div class="ez-label">
        <span class="ez-type-${tc}">${m.type}</span>
        <span style="color:var(--text2)">${m.w1_rn.toLocaleString()} → ${m.w2_rn.toLocaleString()}</span>
      </div>
      <div class="ez-bar-track">
        <div class="ez-bar-w1 fill-${tc}" style="width:${p1}%"></div>
        <div class="ez-bar-w2 fill-${tc}" style="width:${p2}%"></div>
      </div>
      <div class="ez-pct-row">
        <span>${p1}% → ${p2}%</span>
        <span class="ez-pct-wow ${pwCls}">${pwSign}${pwow}pp</span>
      </div>
    </div>`;
  });
  eH+=`</div>`;
});
document.getElementById('ez-grid').innerHTML=eH;
</script>
</body>
</html>