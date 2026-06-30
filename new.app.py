import streamlit as st
import pandas as pd
import json
import re
from datetime import datetime

st.set_page_config(page_title="OTA 週報數據更新器", layout="centered")

st.title("📊 OTA 週報網頁數據更新器 (精準欄位模糊對齊版)")
st.write("此版本強化了 MM 姓名的動態比對與欄位防呆，確保 CSV 原始明細能精準映射至網頁結構。")

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
  if(t==='rev')return'<span class="num-rev">'+Number(v).toLocaleString(\'en-US\',{maximumFractionDigits:2})+'</span>';
  if(t==='adr')return'<span class="num-adr">'+Number(v).toLocaleString(\'en-US\',{minimumFractionDigits:2,maximumFractionDigits:2})+'</span>';
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
document.getElementById(\'mm-summary\').innerHTML=
