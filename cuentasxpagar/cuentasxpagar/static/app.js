function buscarResultados(fila) {
    console.log("buscarResultados");
    let input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("buscar");
    filter = input.value.toUpperCase();
    table = document.getElementById("tablaResultados");
    tr = table.getElementsByTagName("tr");
    for (i = 0; i < tr.length; i++) {
      td = tr[i].getElementsByTagName("td")[fila];
      if (td) {
        txtValue = td.textContent || td.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }       
    }
  }

function cleanAsiento() {
    document.getElementById('fechaDesde').value = "";
    document.getElementById('fechaHasta').value = "";
}

function onChangeFechaDesdeAsiento(){
  document.getElementById('fechaHasta').disabled = false;
  document.getElementById('fechaHasta').min = document.getElementById('fechaDesde').value;
}