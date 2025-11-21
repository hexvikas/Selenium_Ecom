const { tcNames, tcTimes, tcStatus } = window.reportData;

// Bar chart: execution time
new Chart(document.getElementById("timeChart"), {
  type: "bar",
  data: {
    labels: tcNames,
    datasets: [{
      label: "Execution Time (seconds)",
      data: tcTimes
    }]
  },
  options: {
    responsive: true,
    plugins: {
      legend: { display: true }
    },
    scales: {
      y: { beginAtZero: true }
    }
  }
});

// Doughnut chart: pass vs fail
const passCount = tcStatus.filter(s => s === "PASS").length;
const failCount = tcStatus.filter(s => s === "FAIL").length;

new Chart(document.getElementById("statusChart"), {
  type: "doughnut",
  data: {
    labels: ["PASS", "FAIL"],
    datasets: [{
      data: [passCount, failCount]
    }]
  },
  options: {
    responsive: true,
    plugins: {
      legend: { display: true }
    }
  }
});
