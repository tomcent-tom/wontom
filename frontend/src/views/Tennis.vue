<template>
  <div class="Tennis">
    <div class="cont">
      <div class="row">
        <div class="col s2">Date</div>
        <div class="col s2">Beginner</div>
        <div class="col s2">Low-Intermediate</div>
        <div class="col s2">Intermediate</div>
        <div class="col s2">High-Intermediate</div>
        <div class="col s2">Advanced</div>
      </div>
      <div class="row" v-for="date in dates" v-bind:key="date">
        <div class="col s2">
          <h6>{{date | formatDate}}</h6>
        </div>
        <div class="col s2">
          <div v-for="tenInfo in perLevelDay(tennisInfo, 'BEGINNERS', date)" v-bind:key="tenInfo.id">
            <TennisCard v-bind:tennisInfo="tenInfo"></TennisCard>
          </div>
          
        </div>
        <div class="col s2">
          <div v-for="tenInfo in perLevelDay(tennisInfo, 'LOW INTERMEDIATE', date)" v-bind:key="tenInfo.id">
            <TennisCard v-bind:tennisInfo="tenInfo"></TennisCard>
          </div>
        </div>
        <div class="col s2">
          <div v-for="tenInfo in perLevelDay(tennisInfo, 'INTERMEDIATE', date)" v-bind:key="tenInfo.id">
            <TennisCard v-bind:tennisInfo="tenInfo"></TennisCard>
          </div>
        </div>
        <div class="col s2">
          <div v-for="tenInfo in perLevelDay(tennisInfo, 'HIGH INTERMEDIATE', date)" v-bind:key="tenInfo.id">
            <TennisCard v-bind:tennisInfo="tenInfo"></TennisCard>
          </div>
        </div>
        <div class="col s2">
          <div v-for="tenInfo in perLevelDay(tennisInfo, 'ADVANCED', date)" v-bind:key="tenInfo.id">
            <TennisCard v-bind:tennisInfo="tenInfo"></TennisCard>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import TennisCard from "@/components/TennisCard.vue";
import axios from "axios";

function getDate(el) {
  return Date.parse(el["date"]);
}

function dayOfWeekAsString(dayIndex) {
  return ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"][dayIndex];
}

export default {
  name: "Tennis",
  components: {
    TennisCard
  },
  data() {
    return {
      tennisInfo: [],
      dates: []
    };
  },
  mounted() {
    axios.get("http://127.0.0.1:5000/tennisData").then(response => {
      this.tennisInfo = response.data;
      this.dates = [...new Set(this.tennisInfo.map(getDate))].sort();
    });
  },
  filters: {
    formatDate: function(date) {
      let d = new Date(date);
      let dateString = dayOfWeekAsString(d.getDay()) + " " + d.toLocaleDateString("en-AU");
      return dateString;
    }
  },
  methods: {
    perLevelDay: function(arr, level, date) {
      return arr.filter(function(el) {
        let d = Date.parse(el["date"]);
        return el["level"] == level && d == date;
      });
    }
  }
};
</script>

<style>
.cont {
  padding-left: 30px;
}
</style>
