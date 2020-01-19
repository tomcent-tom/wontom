<template>
  <div class="tenniscard">
    <div class="card">
      <div class="card-content">
        <span>
          <b>{{tennisInfo.time}}</b>
        </span>
        <br />
        <span>
          <i>{{tennisInfo.place}}</i>
        </span>
        <br />
        <span class="blue-text text-darken-2">{{tennisInfo.remaining}} places left.</span>
        <div class="valign-wrapper">
          <a class="btn-floating waves-effect waves-light red right-align" v-bind:class="{ disabled: tennisInfo.remaining==0}" v-on:click="openNewTab('https://jensenstennis.intrac.com.au/tennis/clubevent.cfm?event='+tennisInfo.game)">
            <i class="material-icons">add</i>
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "TennisCard",
  props: ["tennisInfo"],
  methods: {
    openNewTab: function(url) {
      var win = window.open(url, '_blank');
      win.focus();
    }
  }
};
</script>