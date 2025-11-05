"""
Flask app that serves a single-page sorting animation.
Run: python3 sorting_animation_flask.py
Open: http://127.0.0.1:5000

This file serves an HTML page which performs the animation in-browser using JavaScript.
You can choose algorithm (Bubble, Quick, Merge, Insertion), array size, and speed.
"""
from flask import Flask, render_template_string

app = Flask(__name__)

TEMPLATE = '''
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Sorting Algorithm Visualizer</title>
  <style>
    :root{--bg:#0f1724;--card:#0b1220;--accent:#7dd3fc}
    html,body{height:100%;margin:0;font-family:Inter,system-ui,-apple-system,Segoe UI,Roboto,"Helvetica Neue",Arial}
    body{background:linear-gradient(180deg,#071024 0%, #081326 100%);color:#e6eef6;display:flex;align-items:center;justify-content:center;padding:16px}
    .app{width:100%;max-width:1100px;background:rgba(255,255,255,0.02);border-radius:12px;padding:18px;box-shadow:0 8px 30px rgba(2,6,23,0.6)}
    header{display:flex;align-items:center;gap:16px;margin-bottom:14px}
    h1{font-size:18px;margin:0}
    .controls{display:flex;gap:10px;flex-wrap:wrap;align-items:center}
    select,input[type=range],button{background:transparent;color:inherit;border:1px solid rgba(255,255,255,0.06);padding:8px;border-radius:8px}
    .row{display:flex;gap:12px;align-items:center}
    #canvas{height:420px;background:linear-gradient(180deg, rgba(255,255,255,0.01), rgba(255,255,255,0.00));border-radius:8px;overflow:hidden;display:flex;align-items:flex-end;padding:12px}
    .bar{margin:0 1px;border-radius:3px}
    footer{margin-top:12px;font-size:13px;color:rgba(230,238,246,0.75)}
    label{font-size:13px}
    .small{font-size:12px;color:#9fb7c9}
  </style>
</head>
<body>
  <div class="app">
    <header>
      <h1>Sorting Visualizer — pick an algorithm and enjoy the chaos → order</h1>
      <div class="controls">
        <div class="row">
          <label>Algorithm:</label>
          <select id="algo">
            <option>Bubble</option>
            <option>Insertion</option>
            <option>Merge</option>
            <option selected>Quick</option>
            <option>Heap</option>
          </select>
        </div>
        <div class="row">
          <label>Size:</label>
          <input id="size" type="range" min="10" max="160" value="60" />
          <span class="small" id="sizeVal">60</span>
        </div>
        <div class="row">
          <label>Speed:</label>
          <input id="speed" type="range" min="1" max="1000" value="80" />
          <span class="small" id="speedVal">80 ms</span>
        </div>
        <div class="row">
          <button id="shuffle">Shuffle</button>
          <button id="start">Start</button>
          <button id="stop">Stop</button>
        </div>
      </div>
    </header>

    <div id="canvas"></div>
    <footer>
      <div>Visualization shows element comparisons and swaps. Implemented with plain JavaScript for smooth animation.</div>
    </footer>
  </div>

<script>
// Utilities
const canvas = document.getElementById('canvas');
const sizeSlider = document.getElementById('size');
const sizeVal = document.getElementById('sizeVal');
const speedSlider = document.getElementById('speed');
const speedVal = document.getElementById('speedVal');
const algoSelect = document.getElementById('algo');
const shuffleBtn = document.getElementById('shuffle');
const startBtn = document.getElementById('start');
const stopBtn = document.getElementById('stop');

let array = [];
let bars = [];
let running = false;
let stopRequested = false;

function randInt(min, max){ return Math.floor(Math.random()*(max-min+1))+min }

function buildArray(n){
  array = new Array(n).fill(0).map(()=>randInt(5, 100));
  render();
}

function render(){
  canvas.innerHTML = '';
  bars = [];
  const w = canvas.clientWidth;
  const barWidth = Math.max(2, Math.floor(w / array.length) - 2);
  for(let i=0;i<array.length;i++){
    const b = document.createElement('div');
    b.className = 'bar';
    b.style.width = barWidth + 'px';
    b.style.height = (array[i]/100*100) + '%';
    b.style.background = `linear-gradient(180deg, rgba(125,211,252,0.95), rgba(125,211,252,0.6))`;
    canvas.appendChild(b);
    bars.push(b);
  }
}

function setBar(i, value){
  array[i] = value;
  bars[i].style.height = (value/100*100) + '%';
}

function color(i, col){
  bars[i].style.boxShadow = `0 0 6px ${col}`;
}

function swap(i,j){
  const tmp = array[i];
  array[i] = array[j];
  array[j] = tmp;
  const h1 = bars[i].style.height;
  bars[i].style.height = bars[j].style.height;
  bars[j].style.height = h1;
}

async function sleep(ms){
  return new Promise(resolve=>setTimeout(resolve, ms));
}

function getDelay(){
  return Math.max(1, parseInt(speedSlider.value));
}

// Sorting algorithms implemented as async generators/async functions that yield control for animation

async function bubbleSort(){
  const n = array.length;
  for(let i=0;i<n-1;i++){
    for(let j=0;j<n-1-i;j++){
      if(stopRequested) return;
      color(j, 'rgba(255,255,255,0.9)');
      color(j+1, 'rgba(255,255,255,0.9)');
      await sleep(getDelay());
      if(array[j] > array[j+1]){
        swap(j, j+1);
      }
      color(j, 'transparent');
      color(j+1, 'transparent');
    }
  }
}

async function insertionSort(){
  for(let i=1;i<array.length;i++){
    if(stopRequested) return;
    let key = array[i];
    let j = i-1;
    color(i, 'rgba(255,255,255,0.9)');
    await sleep(getDelay());
    while(j>=0 && array[j] > key){
      if(stopRequested) return;
      setBar(j+1, array[j]);
      color(j, 'rgba(255,255,255,0.9)');
      await sleep(getDelay());
      color(j, 'transparent');
      j--;
    }
    setBar(j+1, key);
    color(i, 'transparent');
  }
}

async function mergeSortWrapper(){
  await mergeSort(0, array.length-1);
}

async function mergeSort(l, r){
  if(stopRequested) return;
  if(l>=r) return;
  const m = Math.floor((l+r)/2);
  await mergeSort(l,m);
  await mergeSort(m+1,r);
  const a = [];
  let i=l,j=m+1;
  while(i<=m && j<=r){
    if(stopRequested) return;
    color(i, 'rgba(255,255,255,0.9)');
    color(j, 'rgba(255,255,255,0.9)');
    await sleep(getDelay());
    if(array[i] <= array[j]){ a.push(array[i++]); } else { a.push(array[j++]); }
    color(i-1, 'transparent');
    color(j-1, 'transparent');
  }
  while(i<=m){ a.push(array[i++]); }
  while(j<=r){ a.push(array[j++]); }
  for(let k=0;k<a.length;k++){
    if(stopRequested) return;
    setBar(l+k, a[k]);
    await sleep(getDelay());
  }
}

async function quickSortWrapper(){
  await quickSort(0, array.length-1);
}

async function quickSort(low, high){
  if(stopRequested) return;
  if(low < high){
    const p = await partition(low, high);
    await quickSort(low, p-1);
    await quickSort(p+1, high);
  }
}

async function partition(low, high){
  let pivot = array[high];
  color(high, 'rgba(255,200,90,0.95)');
  let i = low;
  for(let j=low;j<high;j++){
    if(stopRequested) return high;
    color(j, 'rgba(255,255,255,0.9)');
    await sleep(getDelay());
    if(array[j] < pivot){
      swap(i,j);
      color(i, 'rgba(120,255,180,0.9)');
      await sleep(getDelay());
      color(i, 'transparent');
      i++;
    }
    color(j, 'transparent');
  }
  swap(i, high);
  color(high, 'transparent');
  return i;
}

// Heap sort
async function heapSort(){
  const n = array.length;
  for(let i=Math.floor(n/2)-1;i>=0;i--){
    await heapify(n, i);
    if(stopRequested) return;
  }
  for(let i=n-1;i>0;i--){
    if(stopRequested) return;
    swap(0,i);
    await sleep(getDelay());
    await heapify(i, 0);
  }
}

async function heapify(n, i){
  let largest = i;
  const l = 2*i+1;
  const r = 2*i+2;
  if(l<n){ color(l, 'rgba(255,255,255,0.9)'); }
  if(r<n){ color(r, 'rgba(255,255,255,0.9)'); }
  await sleep(getDelay());
  if(l<n && array[l] > array[largest]) largest = l;
  if(r<n && array[r] > array[largest]) largest = r;
  if(l<n){ color(l, 'transparent'); }
  if(r<n){ color(r, 'transparent'); }
  if(largest != i){
    swap(i, largest);
    await heapify(n, largest);
  }
}

async function runAlgorithm(){
  running = true; stopRequested = false;
  const algo = algoSelect.value;
  try{
    if(algo === 'Bubble') await bubbleSort();
    else if(algo === 'Insertion') await insertionSort();
    else if(algo === 'Merge') await mergeSortWrapper();
    else if(algo === 'Quick') await quickSortWrapper();
    else if(algo === 'Heap') await heapSort();
  }finally{
    running = false;
  }
}

// Controls wiring
sizeSlider.addEventListener('input', ()=>{ sizeVal.textContent = sizeSlider.value; buildArray(parseInt(sizeSlider.value)); });
speedSlider.addEventListener('input', ()=>{ speedVal.textContent = speedSlider.value + ' ms'; });
shuffleBtn.addEventListener('click', ()=>{ buildArray(parseInt(sizeSlider.value)); });
startBtn.addEventListener('click', ()=>{ if(!running){ runAlgorithm(); } });
stopBtn.addEventListener('click', ()=>{ stopRequested = true; });

// initialise
window.addEventListener('load', ()=>{ sizeVal.textContent = sizeSlider.value; speedVal.textContent = speedSlider.value + ' ms'; buildArray(parseInt(sizeSlider.value)); });

// Resize-friendly: re-render on window resize to recalc bar widths
let resizeTimer = null;
window.addEventListener('resize', ()=>{ clearTimeout(resizeTimer); resizeTimer = setTimeout(()=>render(),150); });

</script>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(TEMPLATE)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)

