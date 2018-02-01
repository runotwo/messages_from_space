Vue.component('Message', {
    props: ['id', 'date', 'text'],
    template: '<div class="alert alert-primary" v-bind:data-id="id">\n' +
    '    <div class="row align-items-center">\n' +
    '        <div class="col">\n' +
    '            {{ text }}<br>\n' +
    '            <small class="text-muted">{{ date }}</small>\n' +
    '        </div>\n' +
    '        <button type="button" class="btn btn-primary col-2 align-self-center" @click="clickRead($event)">Прочитано</button>\n' +
    '    </div>\n' +
    '</div>',
    methods: {
        clickRead: function (e) {
            elem = e.target.offsetParent;
            appId = ($(elem).index());
            serverId = $(elem).data('id');
            app.messages.splice(appId, 1);
            axios.get('api/mark_read?id=' + serverId)
                .catch(function (error) {
                    console.log(error)
                });
        }
    }
});

var app = new Vue({
    el: '#app',
    data: {
        a: 1,
        messages: []
    },
    template: '<div><message v-for="message in messages" :id="message.id" :date="message.date" :text="message.text"></message></div>',
    methods: {
        requestNewMessages: function (lastId) {
            console.log('!');
            var messages_mas = this.messages;
            axios.get('api/get_messages?last_id=' + lastId)
                .then(function (response) {
                    for (i in response.data)
                        messages_mas.push(response.data[i])
                }).catch(function (error) {
                console.log(error)
            });
        }

    }
});

function getLastId(arr) {
    if (arr.length) {
        return arr[arr.length - 1]['id'];
    }
    else {
        return 0;
    }
}

app.requestNewMessages(getLastId(app.messages))

window.setInterval(function () {
    app.requestNewMessages(getLastId(app.messages))
}, 10000);
