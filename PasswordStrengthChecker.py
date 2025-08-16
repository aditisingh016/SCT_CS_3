<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Password Strength Checker</title>
  <style>
    body { font-family: Arial, sans-serif; padding: 2rem; background:#0f1220; color:#fff; }
    input { padding: 10px; font-size: 16px; width: 300px; border-radius: 6px; border: none; }
    .meter { margin-top: 10px; height: 10px; background: #333; border-radius: 6px; overflow: hidden; }
    .fill { height: 100%; width: 0%; transition: width .3s ease; }
    .weak .fill { background: red; }
    .medium .fill { background: orange; }
    .strong .fill { background: limegreen; }
    .very-strong .fill { background: cyan; }
    #tips { margin-top: 10px; }
  </style>
</head>
<body>
  <h1>🔐 Password Strength Checker</h1>
  <input type="password" id="pwd" placeholder="Enter password..." />
  <div id="bar" class="meter"><div class="fill"></div></div>
  <p id="scoreLabel"></p>
  <ul id="tips"></ul>

  <script>
    const pwd = document.getElementById('pwd');
    const bar = document.getElementById('bar');
    const fill = document.querySelector('.fill');
    const label = document.getElementById('scoreLabel');
    const tips = document.getElementById('tips');

    pwd.addEventListener('input', () => {
      const password = pwd.value;
      const result = assess(password);
      render(result);
    });

    function assess(password){
      const hasLower = /[a-z]/.test(password);
      const hasUpper = /[A-Z]/.test(password);
      const hasNum = /[0-9]/.test(password);
      const hasSpec = /[ !"#$%&'()*+,\-./:;<=>?@[\\\]^_`{|}~]/.test(password);

      let score = 0;
      if (password.length >= 16) score += 40;
      else if (password.length >= 12) score += 30;
      else if (password.length >= 8) score += 20;

      if (hasLower) score += 15;
      if (hasUpper) score += 15;
      if (hasNum) score += 15;
      if (hasSpec) score += 15;
      if ([hasLower, hasUpper, hasNum, hasSpec].filter(Boolean).length >= 3) score += 10;

      let label = "Weak", bucket = "weak";
      if (score >= 90){ label="Very Strong"; bucket="very-strong"; }
      else if (score >= 70){ label="Strong"; bucket="strong"; }
      else if (score >= 40){ label="Medium"; bucket="medium"; }

      const suggestions = [];
      if (password.length < 12) suggestions.push("Increase length to at least 12 characters.");
      if (!hasLower) suggestions.push("Add lowercase letters.");
      if (!hasUpper) suggestions.push("Add uppercase letters.");
      if (!hasNum) suggestions.push("Add numbers.");
      if (!hasSpec) suggestions.push("Add special characters.");

      return {score,label,bucket,suggestions};
    }

    function render(result){
      bar.className = "meter " + result.bucket;
      fill.style.width = result.score + "%";
      label.textContent = `Score: ${result.score} — ${result.label}`;
      tips.innerHTML = result.suggestions.map(s => `<li>${s}</li>`).join('');
    }
  </script>
</body>
</html>
