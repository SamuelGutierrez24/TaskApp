function nameSearch() {
    // Declare variables
    var input, filter, table, tr, th, i, txtValue;
    // search field
    input = document.getElementById('idS');
    // get the text on the search field
    filter = input.value.toUpperCase();
    // get table
    table = document.getElementById("tTable");
    // get all rows inside the table
    tr = table.getElementsByTagName('tr');
    // Loop through all list items, and hide those who don't match the search query
    for (i = 1; i < tr.length; i++) {
      // get the firts th from the ith tr
      td = tr[i].getElementsByTagName("td")[0];
      // extract the text inside th
      txtValue = td.textContent || td.innerText;
      // does the th element contains the filter?
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
          // if the index bigger that -1 the th element contains the filter
          tr[i].style.display = "";
      } else {
          // if the index is -1 the th element does not contains the filter
          tr[i].style.display = "none";
      }
    }
  }
  function descSearch() {
    // Declare variables
    var input, filter, table, tr, th, i, txtValue;
    // search field
    input = document.getElementById('idSd');
    // get the text on the search field
    filter = input.value.toUpperCase();
    // get table
    table = document.getElementById("tTable");
    // get all rows inside the table
    tr = table.getElementsByTagName('tr');
    // Loop through all list items, and hide those who don't match the search query
    for (i = 1; i < tr.length; i++) {
      // get the firts th from the ith tr
      td = tr[i].getElementsByTagName("td")[1];
      // extract the text inside th
      txtValue = td.textContent || td.innerText;
      // does the th element contains the filter?
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
          // if the index bigger that -1 the th element contains the filter
          tr[i].style.display = "";
      } else {
          // if the index is -1 the th element does not contains the filter
          tr[i].style.display = "none";
      }
    }
  }
  function catSearch() {
    // Declare variables
    var input, filter, table, tr, th, i, txtValue;
    // search field
    input = document.getElementById('id_category');
    // get the text on the search field
    filter = input.value.toUpperCase();
    // get table
    table = document.getElementById("tTable");
    // get all rows inside the table
    tr = table.getElementsByTagName('tr');
    // Loop through all list items, and hide those who don't match the search query
    for (i = 1; i < tr.length; i++) {
      // get the firts th from the ith tr
      td = tr[i].getElementsByTagName("td")[2];
      // extract the text inside th
      txtValue = td.textContent || td.innerText;
      // does the th element contains the filter?
      if(txtValue.length>0){
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            // if the index bigger that -1 the th element contains the filter
            tr[i].style.display = "";
        } else {
            // if the index is -1 the th element does not contains the filter
            tr[i].style.display = "none";
        }
      }
      
    }
  }
  function stateSearch() {
    // Declare variables
    var input, filter, table, tr, th, i, txtValue;
    // search field
    input = document.getElementById('id_taskState');
    // get the text on the search field
    filter = input.value.toUpperCase();
    // get table
    table = document.getElementById("tTable");
    // get all rows inside the table
    tr = table.getElementsByTagName('tr');
    // Loop through all list items, and hide those who don't match the search query
    for (i = 1; i < tr.length; i++) {
        // get the firts th from the ith tr
        td = tr[i].getElementsByTagName("td")[3];
        // extract the text inside th
        txtValue = td.textContent || td.innerText;
        // does the th element contains the filter?
        if (txtValue.toUpperCase().indexOf(filter) > -1 || filter==5) {
            // if the index bigger that -1 the th element contains the filter
            tr[i].style.display = "";
        } 
        else {
            // if the index is -1 the th element does not contains the filter
            tr[i].style.display = "none";
        }
      
    }
  }

  function dates() {
    // Declare variables
    var input, filter, table, tr, th, i, txtValue;
    // search field
    var input1 = document.getElementById('id_startDate');
    var filter1 = input1.value;
    var input2 = document.getElementById('id_endDate');
    var filter2 = input2.value;


    table = document.getElementById("tTable");
    // get all rows inside the table
    tr = table.getElementsByTagName('tr');
    // Loop through all list items, and hide those who don't match the search query
    for (i = 1; i < tr.length; i++) {
        // get the firts th from the ith tr
        td = tr[i].getElementsByTagName("td")[4];
        // extract the text inside th
        txtValue = td.textContent || td.innerText;
        date = Date.parse(txtValue);
        filtDate1 = Date.parse(filter1);
        filtDate2 = Date.parse(filter2);
        // does the th element contains the filter?
        if (filtDate1 <= date && filtDate2>=date) {
            // if the index bigger that -1 the th element contains the filter
            tr[i].style.display = "";
        } 
        else {
            // if the index is -1 the th element does not contains the filter
            tr[i].style.display = "none";
        }
      
    }
}