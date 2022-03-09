// Datatable
$(document).ready(function () {

    var items = [];
    var table1 = $('#static-page').DataTable();
    var table2 = $('#non-static-page').DataTable({
        ajax: {
            url: "/data/",
            type: "POST",
            data: {
                'items': JSON.stringify(items)
            }
        },
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        columns: [
            {"data": "skill"},
            {"data": "weight"},
        ],
        order: [[ 1, "asc" ]]
    });

    table2.on('click', 'tbody tr' ,function() {
        var $row = $(this);
        var addRow = table2.row($row);
        items.push(addRow.data());
        refreshTable();
        table1.row.add([
            addRow.data().skill,
            addRow.data().weight
        ]).draw();
    });

    table1.on('click', 'tbody tr' ,function() {
        var $row = $(this);
        var addRow = table1.row($row);
        items = items.filter(function(value, index, arr){ 
            return value.skill != addRow.data()[0];
        });
        refreshTable();
        addRow.remove().draw();
    });

    async function refreshTable() {
        console.log(items);
        table2.destroy();
        table2 = await $('#non-static-page').DataTable({
            ajax: {
                url: "/data/",
                type: "POST",
                data: {
                    'items': JSON.stringify(items)
                }
            },
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            columns: [
                {"data": "skill"},
                {"data": "weight"},
            ],
            order: [[ 1, "asc" ]]
        });
    }
});