document.getElementById("goodsForm").addEventListener("submit", async function (e) {
    e.preventDefault();
  
    const formData = new FormData(e.target);
    const data = Object.fromEntries(formData.entries());
  
    const res = await fetch("http://127.0.0.1:5000/api/goods", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data)
    });
  
    if (res.ok) {
      alert("添加成功！");
      e.target.reset();
    } else {
      alert("提交失败");
    }
  });
  