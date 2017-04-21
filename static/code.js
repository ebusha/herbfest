function init(graph){ // on dom ready

  var cy = cytoscape({
    container: document.getElementById('cy'),
    
    style: cytoscape.stylesheet()
                    .selector('node')
                    .css({
                      'background-color': '#B3767E',
                      'content': 'data(id)'
                    })
                    .selector('edge')
                    .css({
                      'line-color': '#F2B1BA',
                      'target-arrow-color': '#F2B1BA',
                      'width': 2,
                      'target-arrow-shape': 'circle',
                      'opacity': 0.8
                    })
                    .selector(':selected')
                    .css({
                      'background-color': 'black',
                      'line-color': 'black',
                      'target-arrow-color': 'black',
                      'source-arrow-color': 'black',
                      'opacity': 1
                    })
                    .selector('.faded')
                    .css({
                      'opacity': 0.25,
                      'text-opacity': 0
                    }),
    
    elements: graph,
    
    layout: {
      name: 'circle',
      padding: 10
    },
    
    ready: function(){
      // ready 1
    },

    maxZoom: 2,
    minZoom: 0.05
  });
}; // on dom ready
