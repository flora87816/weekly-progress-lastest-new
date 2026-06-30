import streamlit as st
import pandas as pd
import json
import re

st.set_page_config(page_title="OTA 週報數據更新器", layout="centered")

st.title("📊 OTA 週報網頁數據更新器 (CSV 自動計算版)")
st.write("請在下方上傳每週拉出來的數據 CSV 檔，系統會自動完成所有複雜的數據加總與 WoW 計算，並注入你的網頁模板中。")

# 這裡是你精美的 HTML 原始碼模板
HTML_TEMPLATE = """<!DOCTYPE html>
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
const D = __DATA_PLACEHOLDER__;

function n(v,t){
  if(v===null||v===undefined)return'<span class="wow-nt">—</span>';
  if(t==='rn')return'<span class="num-rn">'+Number(v).toLocaleString()+'</span>';
  if(t==='rev')return'<span class="num-rev">'+Number(v).toLocaleString(\'en-US\',{maximumFractionDigits:0})+'</span>';
  if(t==='adr')return'<span class="num-adr">'+Number(v).toLocaleString(\'en-US\',{minimumFractionDigits:0,maximumFractionDigits:0})+'</span>';
  return v;
}
function w(v){
  if(v===null||v===undefined||isNaN(v)||!isFinite(v))return'<span class="wow-nt">—</span>';
  const p=(v*100).toFixed(1),cls=v>=0?\'wow-up\':\'wow-dn\',s=v>=0?\'+\':\'\';
  return`<span class="${cls}">${s}${p}%</span>`;
}
function showSection(name,el){
  document.querySelectorAll(\'.section\').forEach(s=>s.classList.remove(\'active\'));
  document.querySelectorAll(\'.tab\').forEach(t=>t.classList.remove(\'active\'));
  document.getElementById(\'sec-\'+name).classList.add(\'active\');
  el.classList.add(\'active\');
}

// Labels
[\'mm\',\'city\',\'site\'].forEach(k=>{
  const a=document.getElementById(\'lbl-w1-\'+k);
  const b=document.getElementById(\'lbl-w2-\'+k);
  if(a)a.textContent=D.week1_label;
  if(b)b.textContent=D.week2_label;
});
document.getElementById(\'reportMeta\').textContent=\'Book Day \'+D.report_date;
document.getElementById(\'weekBadge\').textContent=D.week1_label+\' → \'+D.week2_label;

// Summary
const tW1rn=D.mm_overview.reduce((s,m)=>s+m.w1_rn,0);
const tW2rn=D.mm_overview.reduce((s,m)=>s+m.w2_rn,0);
const tW1rev=D.mm_overview.reduce((s,m)=>s+m.w1_rev,0);
const tW2rev=D.mm_overview.reduce((s,m)=>s+m.w2_rev,0);
const wRn=tW1rn?(tW2rn-tW1rn)/tW1rn:0,wRev=tW1rev?(tW2rev-tW1rev)/tW1rev:0;
document.getElementById(\'mm-summary\').innerHTML=[
  {l:D.week1_label+\' RN\',v:tW1rn.toLocaleString(),w:null},
  {l:D.week2_label+\' RN\',v:tW2rn.toLocaleString(),w:wRn},
  {l:D.week1_label+\' REV (TWD)\',v:(tW1rev/1e6).toFixed(2)+\'M\',w:null},
  {l:D.week2_label+\' REV (TWD)\',v:(tW2rev/1e6).toFixed(2)+\'M\',w:wRev},
].map(s=>`<div class="summary-card">
  <div class="summary-card-label">${s.l}</div>
  <div class="summary-card-value">${s.v}</div>
  ${s.w!==null?`<div class="summary-card-wow ${s.w>=0?\'wow-up\':\'wow-dn\'}">${s.w>=0?\'+\':\'\'}${(s.w*100).toFixed(1)}% WoW</div>`:''}
</div>`).join(\'\');

// MM table
let mmH=\'\';
D.mm_overview.forEach(m=>{
  const fname=m.name.split(\' \')[0];
  const cname=m.name.match(/（([^）]+)）/)?m.name.match(/（([^）]+)）/)[1]:\'\';
  mmH+=`<tr>
    <td><b>${fname}</b> <span style="color:var(--text3);font-size:11px">${cname}</span></td>
    <td>${n(m.w1_rn,\'rn\')}</td><td>${n(m.w1_rev,\'rev\')}</td><td>${n(m.w1_adr,\'adr\')}</td>
    <td>${n(m.w2_rn,\'rn\')}</td><td>${n(m.w2_rev,\'rev\')}</td><td>${n(m.w2_adr,\'adr\')}</td>
    <td>${w(m.wow_rn)}</td><td>${w(m.wow_rev)}</td><td>${w(m.wow_adr)}</td>
  </tr>`;
});
const tAdr1=tW1rn?tW1rev/tW1rn:0,tAdr2=tW2rn?tW2rev/tW2rn:0;
mmH+=`<tr class="row-total">
  <td>Others 總計</td>
  <td>${n(tW1rn,\'rn\')}</td><td>${n(tW1rev,\'rev\')}</td><td>${n(tAdr1,\'adr\')}</td>
  <td>${n(tW2rn,\'rn\')}</td><td>${n(tW2rev,\'rev\')}</td><td>${n(tAdr2,\'adr\')}</td>
  <td>${w(wRn)}</td><td>${w(wRev)}</td><td>${w(tAdr1?(tAdr2-tAdr1)/tAdr1:0)}</td>
</tr>`;
document.getElementById(\'mm-tbody\').innerHTML=mmH;

// City+Star table
let cH=\'\';
D.city_star_overview.forEach(c=>{
  cH+=`<tr class="row-city">
    <td>${c.city}</td>
    <td>${n(c.w1_rn,\'rn\')}</td><td>${n(c.w1_rev,\'rev\')}</td><td>${n(c.w1_adr,\'adr\')}</td>
    <td>${n(c.w2_rn,\'rn\')}</td><td>${n(c.w2_rev,\'rev\')}</td><td>${n(c.w2_adr,\'adr\')}</td>
    <td>${w(c.wow_rn)}</td><td>${w(c.wow_rev)}</td><td>${w(c.wow_adr)}</td>
  </tr>`;
  c.stars.forEach(s=>{
    cH+=`<tr class="row-star">
      <td>${\'★\'.repeat(s.star)} ${s.star}星</td>
      <td>${n(s.w1_rn,\'rn\')}</td><td>${n(s.w1_rev,\'rev\')}</td><td>${n(s.w1_adr,\'adr\')}</td>
      <td>${n(s.w2_rn,\'rn\')}</td><td>${n(s.w2_rev,\'rev\')}</td><td>${n(s.w2_adr,\'adr\')}</td>
      <td>${w(s.wow_rn)}</td><td>${w(s.wow_rev)}</td><td>${w(s.wow_adr)}</td>
    </tr>`;
  });
});
document.getElementById(\'city-tbody\').innerHTML=cH;

// Site by city
const cities=Object.keys(D.city_site_overview);
let selCity=cities[0] || '';
function renderSite(city){
  if(!city) return;
  const data=D.city_site_overview[city];
  const rows=data.sites.filter(s=>s.w1_rn>0||s.w2_rn>0).sort((a,b)=>b.w2_rn-a.w2_rn);
  let h=\'\';
  rows.forEach(s=>{
    h+=`<tr>
      <td>${s.site}</td>
      <td>${n(s.w1_rn,\'rn\')}</td><td>${n(s.w1_rev,\'rev\')}</td><td>${n(s.w1_adr,\'adr\')}</td>
      <td>${n(s.w2_rn,\'rn\')}</td><td>${n(s.w2_rev,\'rev\')}</td><td>${n(s.w2_adr,\'adr\')}</td>
      <td>${w(s.wow_rn)}</td><td>${w(s.wow_rev)}</td><td>${w(s.wow_adr)}</td>
    </tr>`;
  });
  const wowTotal=data.total_w1_rn?(data.total_w2_rn-data.total_w1_rn)/data.total_w1_rn:0;
  h+=`<tr class="row-total">
    <td>Total</td>
    <td>${n(data.total_w1_rn,\'rn\')}</td><td>—</td><td>—</td>
    <td>${data.total_w2_rn.toLocaleString()}</td><td>—</td><td>—</td>
    <td>${w(wowTotal)}</td><td>—</td><td>—</td>
  </tr>`;
  document.getElementById(\'site-tbody\').innerHTML=h;
  document.querySelectorAll(\'.city-tab\').forEach(t=>t.classList.toggle(\'active\',t.dataset.city===city));
}
if(cities.length > 0) {
  document.getElementById(\'site-city-tabs\').innerHTML=cities.map(c=>
    `<div class="city-tab${c===selCity?\' active\':\'\'}" data-city="${c}" onclick="selCity=\'${c}\';renderSite(\'${c}\')">${c}</div>`
  ).join(\'\');
  renderSite(selCity);
}

// EZ Share
let eH=\'\';
D.ez_share.forEach(e=>{
  const fname=e.mm.split(\' \')[0];
  const wSign=e.wow_total>=0?\'+\':\'\';
  const wCls=e.wow_total>=0?\'wow-up\':\'wow-dn\';
  eH+=`<div class="ez-card">
    <div class="ez-card-title">${fname}</div>
    <div class="ez-card-total">${e.total_w1.toLocaleString()} → ${e.total_w2.toLocaleString()} RN &nbsp;<span class="${wCls}">${wSign}${e.wow_total}</span></div>`;
  e.maintenance.forEach(m=>{
    const tc=m.type.toLowerCase();
    const p1=(m.w1_pct*100).toFixed(1),p2=(m.w2_pct*100).toFixed(1);
    const pwow=(m.wow_pct*100).toFixed(1);
    const pwCls=m.wow_pct>=0?\'pct-up\':\'pct-dn\';
    const pwSign=m.wow_pct>=0?\'+\':\'\';
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
</html>"""

# 預算安全除法
def safe_wow(w2, w1):
    if w1 == 0 or pd.isna(w1):
        return 0.0
    return float((w2 - w1) / w1)

def safe_adr(rev, rn):
    if rn == 0 or pd.isna(rn):
        return 0.0
    return float(rev / rn)

st.subheader("1. 填寫本週日期標籤")
col1, col2, col3 = st.columns(3)
with col1:
    report_date = st.text_input("報表基準日 (report_date)", value="2026-06-29")
with col2:
    w1_label = st.text_input("前一週區間 (week1_label)", value="6/12-6/18")
with col3:
    w2_label = st.text_input("本週區間 (week2_label)", value="6/19-6/25")

st.subheader("2. 上傳內部數據 CSV 原始檔")
uploaded_file = st.file_uploader("請上傳 OverseaDataMarket 原始 CSV 檔案", type=["csv"])

if uploaded_file is not None:
    try:
        # 讀取 CSV
        df = pd.read_csv(uploaded_file)
        
        # 欄位型態處理
        num_cols = ['W1 RN', 'W1 Revenue', 'W1 ADR', 'W2 RN', 'W2 Revenue', 'W2 ADR']
        for col in num_cols:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col].astype(str).str.replace(',', ''), errors='coerce').fillna(0)

        # ----------------------------------------------------
        # 計算 1: MM 概況
        # ----------------------------------------------------
        mm_gb = df.groupby('MM Name').agg({
            'W1 RN':'sum', 'W1 Revenue':'sum',
            'W2 RN':'sum', 'W2 Revenue':'sum'
        }).reset_index()
        
        mm_overview = []
        for _, row in mm_gb.iterrows():
            w1_rn, w1_rev = row['W1 RN'], row['W1 Revenue']
            w2_rn, w2_rev = row['W2 RN'], row['W2 Revenue']
            w1_adr = safe_adr(w1_rev, w1_rn)
            w2_adr = safe_adr(w2_rev, w2_rn)
            
            mm_overview.append({
                "name": str(row['MM Name']),
                "w1_rn": int(w1_rn), "w1_rev": float(w1_rev), "w1_adr": float(w1_adr),
                "w2_rn": int(w2_rn), "w2_rev": float(w2_rev), "w2_adr": float(w2_adr),
                "wow_rn": safe_wow(w2_rn, w1_rn),
                "wow_rev": safe_wow(w2_rev, w1_rev),
                "wow_adr": safe_wow(w2_adr, w1_adr)
            })
            
        # ----------------------------------------------------
        # 計算 2: 城市 & 星級
        # ----------------------------------------------------
        city_star_overview = []
        cities = df['City'].dropna().unique()
        for city in cities:
            cdf = df[df['City'] == city]
            c_w1_rn, c_w1_rev = cdf['W1 RN'].sum(), cdf['W1 Revenue'].sum()
            c_w2_rn, c_w2_rev = cdf['W2 RN'].sum(), cdf['W2 Revenue'].sum()
            c_w1_adr = safe_adr(c_w1_rev, c_w1_rn)
            c_w2_adr = safe_adr(c_w2_rev, c_w2_rn)
            
            stars_data = []
            stars = sorted(cdf['Star'].dropna().unique())
            for star in stars:
                sdf = cdf[cdf['Star'] == star]
                s_w1_rn, s_w1_rev = sdf['W1 RN'].sum(), sdf['W1 Revenue'].sum()
                s_w2_rn, s_w2_rev = sdf['W2 RN'].sum(), sdf['W2 Revenue'].sum()
                s_w1_adr = safe_adr(s_w1_rev, s_w1_rn)
                s_w2_adr = safe_adr(s_w2_rev, s_w2_rn)
                
                stars_data.append({
                    "star": int(star),
                    "w1_rn": int(s_w1_rn), "w1_rev": float(s_w1_rev), "w1_adr": float(s_w1_adr),
                    "w2_rn": int(s_w2_rn), "w2_rev": float(s_w2_rev), "w2_adr": float(s_w2_adr),
                    "wow_rn": safe_wow(s_w2_rn, s_w1_rn),
                    "wow_rev": safe_wow(s_w2_rev, s_w1_rev),
                    "wow_adr": safe_wow(s_w2_adr, s_w1_adr)
                })
                
            city_star_overview.append({
                "city": str(city),
                "w1_rn": int(c_w1_rn), "w1_rev": float(c_w1_rev), "w1_adr": float(c_w1_adr),
                "w2_rn": int(c_w2_rn), "w2_rev": float(c_w2_rev), "w2_adr": float(c_w2_adr),
                "wow_rn": safe_wow(c_w2_rn, c_w1_rn),
                "wow_rev": safe_wow(c_w2_rev, c_w1_rev),
                "wow_adr": safe_wow(c_w2_adr, c_w1_adr),
                "stars": stars_data
            })

        # ----------------------------------------------------
        # 計算 3: 各國籍 (Site)
        # ----------------------------------------------------
        city_site_overview = {}
        for city in cities:
            cdf = df[df['City'] == city]
            site_gb = cdf.groupby('Nationality').agg({
                'W1 RN':'sum', 'W1 Revenue':'sum',
                'W2 RN':'sum', 'W2 Revenue':'sum'
            }).reset_index()
            
            sites_list = []
            for _, row in site_gb.iterrows():
                sw1_rn, sw1_rev = row['W1 RN'], row['W1 Revenue']
                sw2_rn, sw2_rev = row['W2 RN'], row['W2 Revenue']
                sw1_adr = safe_adr(sw1_rev, sw1_rn)
                sw2_adr = safe_adr(sw2_rev, sw2_rn)
                
                sites_list.append({
                    "site": str(row['Nationality']),
                    "w1_rn": int(sw1_rn), "w1_rev": float(sw1_rev), "w1_adr": float(sw1_adr),
                    "w2_rn": int(sw2_rn), "w2_rev": float(sw2_rev), "w2_adr": float(sw2_adr),
                    "wow_rn": safe_wow(sw2_rn, sw1_rn),
                    "wow_rev": safe_wow(sw2_rev, sw1_rev),
                    "wow_adr": safe_wow(sw2_adr, sw1_adr)
                })
                
            city_site_overview[str(city)] = {
                "sites": sites_list,
                "total_w1_rn": int(cdf['W1 RN'].sum()),
                "total_w2_rn": int(cdf['W2 RN'].sum())
            }

        # ----------------------------------------------------
        # 計算 4: EZ Share
        # ----------------------------------------------------
        ez_share = []
        for mm in df['MM Name'].dropna().unique():
            mdf = df[df['MM Name'] == mm]
            t_w1 = int(mdf['W1 RN'].sum())
            t_w2 = int(mdf['W2 RN'].sum())
            
            maintenance = []
            types = ['HPP', 'HTL', 'SHT']
            for t in types:
                tdf = mdf[mdf['Hotel Property Type'] == t]
                w1_rn = int(tdf['W1 RN'].sum())
                w2_rn = int(tdf['W2 RN'].sum())
                
                w1_pct = float(w1_rn / t_w1) if t_w1 > 0 else 0.0
                y2_pct = float(w2_rn / t_w2) if t_w2 > 0 else 0.0
                
                maintenance.append({
                    "type": t,
                    "w1_rn": w1_rn, "w2_rn": w2_rn,
                    "wow": int(w2_rn - w1_rn),
                    "w1_pct": w1_pct, "w2_pct": y2_pct,
                    "wow_pct": float(y2_pct - w1_pct)
                })
                
            ez_share.append({
                "mm": str(mm),
                "total_w1": t_w1, "total_w2": t_w2,
                "wow_total": int(t_w2 - t_w1),
                "maintenance": maintenance
            })

        # ----------------------------------------------------
        # 打包成最終 JSON
        # ----------------------------------------------------
        final_data = {
            "report_date": report_date,
            "week1_label": w1_label,
            "week2_label": w2_label,
            "mm_overview": mm_overview,
            "city_star_overview": city_star_overview,
            "city_site_overview": city_site_overview,
            "ez_share": ez_share
        }
        
        # 注入並產生 HTML
        final_json_str = json.dumps(final_data, ensure_ascii=False)
        output_html = HTML_TEMPLATE.replace("__DATA_PLACEHOLDER__", final_json_str)
        
        st.success("🎉 CSV 數據加總並計算完成！")
        
        st.download_button(
            label="📥 點此下載更新後的每週報告網頁 (weekly progress.index.html)",
            data=output_html,
            file_name="weekly progress.index.html",
            mime="text/html"
        )
    except Exception as e:
        st.error(f"CSV 檔案結構不合或解析失敗。錯誤訊息: {e}")
