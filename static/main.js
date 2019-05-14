
//<![CDATA[
function toQueryString(obj) {
    var parts = [];
    for (var i in obj) {
        if (obj.hasOwnProperty(i)) {
            parts.push(encodeURIComponent(i) + "=" + encodeURIComponent(obj[i]));
        }
    }
    return parts.join("&");
}
    window.onload=function(){

        var apiURL = '/github'

        /**
         * Actual repo
         */

        var repo = new Vue({

          el: '#repo',

          data: {
            currentRelease: 'Release_',
            release: 'Release_',
            repos: null
          },

          created: function () {
            this.fetchData()
          },

          watch: {
            currentRelease: 'fetchData'
          },

          filters: {
            truncate: function (v) {
              var newline = v.indexOf('\n')
              return newline > 0 ? v.slice(0, newline) : v
            },
            formatDate: function (v) {
              return v.replace(/T|Z/g, ' ')
            }
          },

          methods: {
            fetchData: function () {
              var xhr = new XMLHttpRequest()
              var self = this
              xhr.open('POST', apiURL, true)
              xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
              xhr.onload = function () {
                self.repos = JSON.parse(xhr.responseText).jobs
              }
              xhr.send('release='+self.currentRelease)
            }
          }
        })


    }

//]]>
