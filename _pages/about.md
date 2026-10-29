---
permalink: /
title: "About Me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---
I am a 2nd year CS PhD student in the School of Interactive Computing at<img src="/images/gt-logo.png" alt="Georgia Tech logo" style="height:1.15em; width:auto; vertical-align:-0.19em; margin:0 0.12em 0 0.28em; border-radius:3px;"> Georgia Tech. I am advised by the amazing Professor [Munmun De Choudhury](http://www.munmund.net/index.html) and am a member of the [Social Dynamics and Wellbeing (SocWeb) Lab](https://socweb.cc.gatech.edu/). I obtained my Bachelor's degree in Computer Science (with High Honors) from<img src="/images/dartmouth_logo.png" alt="Dartmouth College logo" style="height:1.15em; width:auto; vertical-align:-0.19em; margin:0 0.12em 0 0.28em; border-radius:3px;">Dartmouth College, where I was fortunate to be advised by Professors [Nicholas Jacobson](https://www.nicholasjacobson.com/) and [Andrew Campbell](https://www.cs.dartmouth.edu/~campbell/).

I am interested in applying **text-based**, **NLP**, and **generative AI** methods to **make clinical care and mental health safer and more efficient**, advancing research at the intersection of **social computing**, **HCI**, and **mental health**. My recent work takes different approaches to accomplish this: from **training open-sourced foundation models for wearable movement data**, to **reconstructing the timelines of patient journeys from messy, unstructured clinical text using LLM-based human-in-the-loop systems**. I aim to build systems that can easily integrate multimodal and fragmented personal health information from a variety of sources, making **personalized, timely, and targeted clinical decision-making** available to anyone.


<style>
.seeking-box {
  border: 2px dashed #b3a369;
  border-radius: 10px;
  padding: 1em 1.3em;
  margin: 2em 0;
  background: rgba(179, 163, 105, 0.09);
  font-size: medium;
  line-height: 1.6;
}
.seeking-box p:last-child { margin-bottom: 0; }
html[data-theme="dark"] .seeking-box {
  border-color: #d4c48a;
  background: rgba(212, 196, 138, 0.10);
}
</style>

<div class="seeking-box" markdown="1">
✨ **I am actively seeking Summer 2027 research internship opportunities in industry.**
If you think my interests in NLP, machine learning for health, LLMs, and human-AI interaction could be a good fit for your team, I would love to connect — please feel free to reach out at
[azhang677@gatech.edu](mailto:azhang677@gatech.edu).
</div>

------

Updates
======

<div style="overflow-y: scroll; height:200px;">
<ul>

<li><p style="font-size:medium;"><b>[May 2026]:</b> My co-first author paper, <b>A Foundation Model for Wearable Movement Data in Mental Health Research</b> has been accepted to <a href="https://www.embs.org/jbhi/">IEEE Journal of Biomedical and Health Informatics (JBHI)</a>! 🥳 🎉</p></li>

<li><p style="font-size:medium;"><b>[August 2025]:</b> Started school as a CS PhD student at the SocWeb Lab at Georgia Tech! Go Jackets! 🐝 🥳 </p></li>

<li><p style="font-size:medium;"><b>[July 2025]:</b> Our work <b>SeePerSea</b>, which I collaborated in my earlier undergraduate years at Dartmouth, has been accepted to IEEE Transactions on Field Robotics 2025 🥳 <a href="https://seepersea.github.io/">Website Link</a></p></li>

<li><p style="font-size:medium;"><b>[June 2025]:</b> Graduated from Dartmouth with a Major in Computer Science and a minor in Environmental Studies! 🌲 🎓 <em>"vox clamantis in deserto" 💚</em></p></li>

<li><p style="font-size:medium;"><b>[June 2025]:</b> Successfully defended my undergraduate thesis in CS at Dartmouth! <b>MotionTeller: Multi-modal Integration of Wearable Time-Series with LLMs for Health and Behavioral Understanding</b>, has been awarded High Honors! Yay! 🥳 Now in review at the Dartmouth Digital Commons</p></li>

<li><p style="font-size:medium;"><b>[April 2025]:</b> I'll be joining Georgia Tech as a CS PhD student in Fall 2025! 🎉 💛</p></li>

<li><p style="font-size:medium;"><b>[November 2024]:</b> Our work, <b>A Foundation Model for Wearable Movement Data in Mental Health Research</b>, is now available as a preprint on <a href="https://arxiv.org/abs/2411.15240">ArXiv</a>! Our model is the first foundation model designed specifically for actigraphy, which is publicly available - pretrained weights, standardized preprocessing scripts, and full model code are released to <a href="https://github.com/njacobsonlab/Pretrained-Actigraphy-Transformer/">GitHub</a></p></li>

</ul>
</div>

------

Publications
======

<style>
.pub-item {
  display: flex;
  align-items: flex-start;
  gap: 1.4em;
  padding: 1.4em 0;
}
.pub-thumb {
  flex: 0 0 22%;
  max-width: 22%;
}
.pub-thumb img {
  width: 100%;
  height: auto;
  object-fit: cover;
  border-radius: 6px;
  border: 1px solid var(--global-border-color);
}
.pub-body {
  flex: 1 1 auto;
  font-size: medium;
  line-height: 1.5;
}
.pub-title {
  font-weight: 700;
  margin: 0 0 0.25em;
}
.pub-authors { margin: 0 0 0.2em; }
.pub-me {
  color: #1c3f94;
  font-weight: 700;
}
html[data-theme="dark"] .pub-me { color: #8fb4ff; }
.pub-venue {
  font-style: italic;
  color: #6b4423;
  margin: 0;
}
html[data-theme="dark"] .pub-venue { color: #c9a17a; }
.pub-links {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5em;
  margin-top: 0.8em;
}
.pub-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.45em;
  padding: 0.35em 0.8em;
  font-size: 0.85em;
  font-weight: 600;
  line-height: 1.4;
  text-decoration: none !important;
  color: var(--global-text-color) !important;
  background: var(--global-bg-color);
  border: 1px solid #b8bcc2;
  border-radius: 8px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.18), 0 1px 1px rgba(0, 0, 0, 0.10);
  transition: all 0.15s ease-in-out;
}
html[data-theme="dark"] .pub-btn {
  border-color: #8b9199;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.45), 0 1px 1px rgba(0, 0, 0, 0.30);
}
.pub-btn:hover {
  border-color: var(--global-link-color);
  color: var(--global-link-color) !important;
  box-shadow: 0 3px 7px rgba(0, 0, 0, 0.22), 0 1px 2px rgba(0, 0, 0, 0.14);
  transform: translateY(-1px);
}
.pub-btn i { font-size: 0.95em; }

/* Selected / All publication toggle */
#publications { scroll-margin-top: 4.5em; }
.pub-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.6em 1em;
  margin: 0.3em 0 0.2em;
}
/* .page__content p sets font-size: 1em, so this needs the extra class to win */
.page__content .pub-note {
  flex: 1 1 auto;
  min-width: 0;
  margin: 0;
  font-size: 0.75em;
  line-height: 1.5;
}
.pub-note a {
  color: var(--global-link-color);
  font-weight: 600;
  text-decoration: none;
}
.pub-note a:hover {
  color: var(--global-link-color-hover);
  text-decoration: underline;
}
.pub-toggle {
  display: inline-flex;
  flex: 0 0 auto;
  margin-left: auto;
  border: 1px solid #b8bcc2;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.18), 0 1px 1px rgba(0, 0, 0, 0.10);
}
html[data-theme="dark"] .pub-toggle { border-color: #8b9199; }
.pub-toggle button {
  font: inherit;
  font-size: 0.85em;
  font-weight: 600;
  line-height: 1.4;
  padding: 0.35em 1.1em;
  border: 0;
  background: var(--global-bg-color);
  color: var(--global-text-color);
  cursor: pointer;
  transition: all 0.15s ease-in-out;
}
.pub-toggle button + button { border-left: 1px solid #b8bcc2; }
html[data-theme="dark"] .pub-toggle button + button { border-left-color: #8b9199; }
.pub-toggle button:hover { color: var(--global-link-color); }
.pub-toggle button[aria-pressed="true"] {
  background: var(--global-text-color);
  color: var(--global-bg-color);
}
.pub-list .pub-item + .pub-item { border-top: 1px solid var(--global-border-color); }
.pub-list[data-view="selected"] .pub-extra { display: none; }

/* Tighter vertical rhythm between sections */
.page__content h1 {
  margin-top: 1.8em;
  margin-bottom: 0.4em;
}
.page__content hr {
  margin: 0.85em 0;
}

/* Research Experiences / Industry / Education rows —
   same column widths and outer edges as .pub-item above */
.row {
  display: flex;
  align-items: center;
  gap: 1.4em;
  padding: 0.4em 0;
}
.row-logo {
  flex: 0 0 22%;
  max-width: 22%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.row-logo img {
  max-width: 90%;
  height: auto;
  object-fit: contain;
}
.row-text {
  flex: 1 1 auto;
  font-size: large;
  line-height: 1.5;
}

@media screen and (max-width: 600px) {
  .pub-bar { flex-wrap: wrap; }
  .pub-item { flex-direction: column; gap: 0.9em; }
  .pub-thumb { flex: 0 0 auto; max-width: 60%; }
  .row { flex-direction: column; align-items: flex-start; gap: 0.8em; }
  .row-logo { flex: 0 0 auto; max-width: 45%; justify-content: flex-start; }
}
</style>

<div class="pub-bar">
  <p class="pub-note">*: Equal contribution. See also my <a href="{{ site.author.googlescholar }}">Google Scholar</a> profile for the most recent publications.</p>
  <div class="pub-toggle" role="group" aria-label="Filter publications">
    <button type="button" data-view="selected" aria-pressed="true">Selected</button>
    <button type="button" data-view="all" aria-pressed="false">All</button>
  </div>
</div>

------

<div class="pub-list" id="pub-list" data-view="selected">
<div class="pub-item">
  <div class="pub-thumb">
    <img src="/images/pub_icons/CliniCIRCA_icon.png?v=2" alt="CliniCIRCA: modular LLM pipeline turning raw EHR narratives into longitudinal patient journeys">
  </div>
  <div class="pub-body">
    <p class="pub-title">CliniCIRCA: A Modular LLM Framework for Constructing Longitudinal Mental Health Patient Journeys from Raw EHR Narratives</p>
    <p class="pub-authors"><span class="pub-me">Aiwei Ivy Zhang</span>, Nimra Ishfaq, Mohit Chandra, Santiago Alvarez Lesmes, Adam Coscia, Khatiya Chelidze Moon, Xiaohan Ding, Munmun De Choudhury</p>
    <p class="pub-venue">In submission, 2026</p>
    <div class="pub-links">
      <a class="pub-btn" href="https://arxiv.org/abs/2609.19585"><i class="fas fa-file-lines"></i> Paper</a>
      <a class="pub-btn" href="https://theivyzhang.github.io/CliniCIRCA-website/"><i class="fas fa-globe"></i> Website</a>
      <a class="pub-btn" href="https://github.com/theivyzhang/CliniCIRCA"><i class="fab fa-github"></i> Code</a>
    </div>
  </div>
</div>
<div class="pub-item">
  <div class="pub-thumb">
    <img src="/images/pub_icons/PAT_Icon.png" alt="PAT model architecture: masked autoencoder pretraining and finetuning">
  </div>
  <div class="pub-body">
    <p class="pub-title">A Foundation Model for Wearable Movement Data in Mental Health Research</p>
    <p class="pub-authors">Franklin Y. Ruan*, <span class="pub-me">Aiwei Ivy Zhang*</span>, Jenny Y. Oh, SouYoung Jin, Nicholas C. Jacobson <br> (* Equal Contribution)</p>
    <p class="pub-venue">IEEE Journal of Biomedical and Health Informatics (JBHI), 2026</p>
    <div class="pub-links">
      <a class="pub-btn" href="https://arxiv.org/abs/2411.15240"><i class="fas fa-file-lines"></i> Paper</a>
      <a class="pub-btn" href="https://theivyzhang.github.io/PAT-website/"><i class="fas fa-globe"></i> Website</a>
      <a class="pub-btn" href="https://github.com/njacobsonlab/Pretrained-Actigraphy-Transformer/"><i class="fab fa-github"></i> Code</a>
    </div>
  </div>
</div>
<div class="pub-item pub-extra">
  <div class="pub-thumb">
    <img src="/images/pub_icons/FrontierCS2.png" alt="FrontierCS 2: a benchmark of open-ended computer science research and development tasks for AI agents">
  </div>
  <div class="pub-body">
    <p class="pub-title">FrontierCS 2: A Benchmark for Computer Science R&amp;D</p>
    <p class="pub-authors">Qiuyang Mang*, Wenhao Chai*, Runyuan He*, Dongruixuan Li*, Zihan Zheng*, Yujun He*, &hellip;, <span class="pub-me">Aiwei Ivy Zhang</span>, &hellip;, Joseph E. Gonzalez, Alvin Cheung <br> (* Equal Contribution; 61 authors)</p>
    <p class="pub-venue">arXiv preprint, 2026</p>
    <div class="pub-links">
      <a class="pub-btn" href="https://arxiv.org/abs/2610.29932"><i class="fas fa-file-lines"></i> Paper</a>
      <a class="pub-btn" href="https://frontier-cs.org/"><i class="fas fa-globe"></i> Website</a>
      <a class="pub-btn" href="https://github.com/FrontierCS/FrontierCS-2"><i class="fab fa-github"></i> Code</a>
    </div>
  </div>
</div>
<div class="pub-item pub-extra">
  <div class="pub-thumb">
    <img src="/images/pub_icons/Symbolic_Music_Language_AAAI_2026_Icon.png" alt="Music generated by LLMs with and without the IoS inspiration-to-structure framework">
  </div>
  <div class="pub-body">
    <p class="pub-title">Is Symbolic Music a Specific Language? Exploring Inspiration-to-Structure Machine Composition via LLMs</p>
    <p class="pub-authors">Zhejing Hu, Yan Liu, Zhi Zhang, <span class="pub-me">Aiwei Zhang</span>, Sheng-hua Zhong, Bruce X.B. Yu, Gong Chen</p>
    <p class="pub-venue">Proceedings of the AAAI Conference on Artificial Intelligence (AAAI), 2026</p>
    <div class="pub-links">
      <a class="pub-btn" href="https://ojs.aaai.org/index.php/AAAI/article/view/37163"><i class="fas fa-file-lines"></i> Paper</a>
    </div>
  </div>
</div>
<div class="pub-item pub-extra">
  <div class="pub-thumb">
    <img src="/images/pub_icons/MotionTeller_Icon.png" alt="MotionTeller architecture: PAT actigraphy embeddings projected into a Gemma-2B decoder-only LLM">
  </div>
  <div class="pub-body">
    <p class="pub-title">MotionTeller: Multi-modal Integration of Wearable Time-Series with LLMs for Health and Behavioral Understanding</p>
    <p class="pub-authors"><span class="pub-me">Aiwei Zhang</span>, Arvind Pillai, Andrew Campbell, Nicholas C. Jacobson</p>
    <p class="pub-venue">Dartmouth Computer Science Senior Theses (High Honors), 2026</p>
    <div class="pub-links">
      <a class="pub-btn" href="https://arxiv.org/abs/2512.21506"><i class="fas fa-file-lines"></i> Paper</a>
    </div>
  </div>
</div>
<div class="pub-item pub-extra">
  <div class="pub-thumb">
    <img src="/images/pub_icons/SeePerSea_Icon.png" alt="SeePerSea autonomous surface vehicles with LiDAR, camera, and GPS/IMU sensor setups">
  </div>
  <div class="pub-body">
    <p class="pub-title">SeePerSea: Multi-modal Perception Dataset of In-water Objects for Autonomous Surface Vehicles</p>
    <p class="pub-authors">Mingi Jeong, Arihant Chadda, Ziang Ren, Luyang Zhao, Haowen Liu, <span class="pub-me">Aiwei Zhang</span>, Yitao Jiang, Sabriel Achong, Samuel Lensgraf, Monika Roznere, Alberto Quattrini Li</p>
    <p class="pub-venue">IEEE Transactions on Field Robotics, 2025</p>
    <div class="pub-links">
      <a class="pub-btn" href="https://ieeexplore.ieee.org/abstract/document/11142348/"><i class="fas fa-file-lines"></i> Paper</a>
      <a class="pub-btn" href="https://seepersea.github.io/"><i class="fas fa-globe"></i> Website</a>
    </div>
  </div>
</div>
<div class="pub-item pub-extra">
  <div class="pub-thumb">
    <img src="/images/pub_icons/ACM_Multimedia_2020_Icon.png" alt="Music style transfer model: feature extraction, domain adaptation, and joint optimization">
  </div>
  <div class="pub-body">
    <p class="pub-title">Make Your Favorite Music Curative: Music Style Transfer for Anxiety Reduction</p>
    <p class="pub-authors">Zhejing Hu, Yan Liu, Gong Chen, Shen-hua Zhong, <span class="pub-me">Aiwei Zhang</span></p>
    <p class="pub-venue">Proceedings of the 28th ACM International Conference on Multimedia (ACM MM), 2020</p>
    <div class="pub-links">
      <a class="pub-btn" href="https://dl.acm.org/doi/abs/10.1145/3394171.3414070"><i class="fas fa-file-lines"></i> Paper</a>
    </div>
  </div>
</div>
</div>

<script>
(function () {
  var list = document.getElementById('pub-list');
  var buttons = document.querySelectorAll('.pub-toggle button');
  Array.prototype.forEach.call(buttons, function (btn) {
    btn.addEventListener('click', function () {
      list.setAttribute('data-view', btn.getAttribute('data-view'));
      Array.prototype.forEach.call(buttons, function (b) {
        b.setAttribute('aria-pressed', b === btn ? 'true' : 'false');
      });
    });
  });
})();
</script>

------

Research Experiences
======

------

<div class="row">
  <span class="row-logo"><img src="/images/gt-logo.png" alt="Georgia Tech logo"></span>
  <span class="row-text"><b>[August 2025 - Present]</b> Graduate Research Assistant at <a href="https://socweb.cc.gatech.edu/">the Social Dynamics and Wellbeing Lab @ Georgia Tech</a>
  <br> Advised by Professor <a href="http://www.munmund.net/index.html">Munmun De Choudhury</a>.</span>
</div>

------

<div class="row">
  <span class="row-logo"><img src="/images/dartmouth_logo.png" alt="Dartmouth College logo"></span>
  <span class="row-text"><b>[March 2025 - August 2025]</b> Research Assistant at <a href="https://healthx-dartmouth.org/">the HealthX Lab @ Dartmouth College</a>
  <br> Advised by Professor <a href="https://www.cs.dartmouth.edu/~campbell/">Andrew T. Campbell</a> and mentored by PhD student <a href="https://arvindpillai.io/">Arvind Pillai</a>.</span>
</div>

------

<div class="row">
  <span class="row-logo"><img src="/images/dartmouth_logo.png" alt="Dartmouth College logo"></span>
  <span class="row-text"><b>[April 2024 - August 2025]</b> Research Assistant at <a href="https://geiselmed.dartmouth.edu/jacobsonlab/">the Jacobson Lab @ Dartmouth Geisel School of Medicine</a>
  <br> Advised by Professor <a href="http://nicholasjacobson.com/">Nicholas C. Jacobson</a>.</span>
</div>

------

<div class="row">
  <span class="row-logo"><img src="/images/dartmouth_logo.png" alt="Dartmouth College logo"></span>
  <span class="row-text"><b>[January 2023 - June 2024]</b> Research Assistant at <a href="https://rlab.cs.dartmouth.edu/">the Dartmouth Reality and Robotics Lab</a>
  <br> Advised by Professor <a href="https://rlab.cs.dartmouth.edu/albertoq/">Alberto Quattrini Li</a>.</span>
</div>

------

Industry
======

------

<div class="row">
  <span class="row-logo"><img src="/images/BCG_logo.png" alt="BCG HK Icon"></span>
  <span class="row-text"><b>[May 2022 - August 2022]</b> Consultant Intern, TMT & FIG groups at <a href="https://www.bcg.com/offices/hong-kong/default">Boston Consulting Group (Hong Kong)</a></span>
</div>

------

Education
======

------

<div class="row">
  <span class="row-logo"><img src="/images/gt-logo.png" alt="Georgia Tech logo"></span>
  <span class="row-text"><b>[August 2025 - Present]</b> Computer Science PhD Student at <a href="https://www.ic.gatech.edu/">the School of Interactive Computing, Georgia Institute of Technology</a></span>
</div>

------

<div class="row">
  <span class="row-logo"><img src="/images/dartmouth_logo.png" alt="Dartmouth Icon"></span>
  <span class="row-text"><b>[September 2021 - June 2025]</b> Undergraduate student, Computer Science major at <a href="https://home.dartmouth.edu/">Dartmouth College</a></span>
</div>

------
