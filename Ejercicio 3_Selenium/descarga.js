
document.getElementById("downloadPdfBtn").addEventListener("click", () => {
  const link = document.createElement("a");

  link.href = "archivos/challenge-covalto.pdf";
  link.download = "Matriz-de-Pruebas.pdf";

  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
});
