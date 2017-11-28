angular.module('tableExample', [])
  .directive('myTable', function () {
    return {
        restrict: 'E, A, C',
        link: function (scope, element, attrs, controller) {
            var dataTable = element.dataTable(scope.options);

            scope.$watch('options.aaData', handleModelUpdates, true);

            function handleModelUpdates(newData) {
                var data = newData || null;
                if (data) {
                    dataTable.fnClearTable();
                    dataTable.fnAddData(data);
                }
            }
        },
        scope: {
            options: "="
        }
    };
  })
  .controller('Ctrl' , function ($scope){
    $scope.options = {
        aoColumns: [{
            "sTitle": "Surname"
        }, {
            "sTitle": "First Name"
        }],
        aoColumnDefs: [{
            "bSortable": false,
            "aTargets": [0, 1]
        }],
        bJQueryUI: true,
        bDestroy: true,
        aaData: [
            ["Webber", "Adam"]
        ]
    };

    $scope.addData = function () {
        $scope.counter = $scope.counter + 1;
        $scope.options.aaData.push([$scope.counter, $scope.counter * 2]);
    };

    $scope.counter = 0;
  })