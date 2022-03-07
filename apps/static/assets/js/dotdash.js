// Datatable
$(document).ready(function () {
    var table1 = $('#static-page').DataTable();
    var table2 = $('#non-static-page').DataTable({
        ajax: {
            url: "/data/",
            type: "POST"
        },
        data: {
            items: getTableData(table1),
            csrfmiddlewaretoken: '{{ csrf_token }}'
        },
        columns: [
            {"data": "skill"},
            {"data": "weight"},
        ]
    });

    $('#non-static-page tbody').on('click', 'tr', function () {
        var rowdata = table2.row( this ).data();
        table1.row.add([
            rowdata.skill,
            rowdata.weight
        ]).draw();
        table2.ajax.reload();
    });
});

function getTableData(temp) {
    data = '[' + temp.columns(0).data()
        .eq(0)        // Reduce the 2D array into a 1D array of data
        .sort()       // Sort data alphabetically
        .unique()     // Reduce to unique values
        .join(',') + ']';
    console.log(data)
    return data;
};


/*$("#customerSearchButton").on("click", function (event) {
    $.ajax({
        url: "",
        type: "post",
        data: { searchText: searchText }
        }).done(function (result) {
        Table.clear().draw();
        Table.rows.add(result).draw();
    })
});*/
