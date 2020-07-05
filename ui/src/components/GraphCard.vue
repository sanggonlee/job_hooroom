<template>
    <div v-if="locations" class="ui card">
        <div class="content">
            <h5 class="header">Locations</h5>
            <p class="card-text">Source:</p>
            <canvas id="location-chart"></canvas>
        </div>
    </div>
    <div v-else-if="employmentTypes" class="ui card">
        <div class="content">
            <h5 class="header">Employment Types</h5>
            <p class="card-text">Source:</p>
            <canvas id="employmentType-chart"></canvas>
        </div>
    </div>
    <div v-else-if="skills" class="ui card">
        <div class="content">
            <h5 class="header">Skills</h5>
            <p class="card-text">Source:</p>
            <canvas id="skill-chart"></canvas>
        </div>
    </div>
    <div v-else-if="isRemote" class="ui card">
        <div class="content">
            <h5 class="header">Remote</h5>
            <p class="card-text">Source:</p>
            <canvas id="remote-chart"></canvas>
        </div>
    </div>
</template>

<script>
import Chart from 'chart.js';

export default {
    name: 'GraphCard',
    props: ['locations', 'employmentTypes', 'skills', 'isRemote'],
    updated() {
        let label = [];
        let value = [];
        let backgroundColor = [];
        
        if (this.locations) {
            for (let i = 0; i < this.locations.length; i++) {
                label.push(this.locations[i].key);
                value.push(this.locations[i].doc_count);
                backgroundColor.push(this.getRandomColor());
            }

            const ctx = document.getElementById('location-chart');

            new Chart(ctx, {
                type: 'horizontalBar',
                data: {
                    labels: label,
                    datasets: [{
                        data: value,
                        backgroundColor: backgroundColor
                    }]
                },
                options: {
                    legend: {
                        display: false
                    },
                    scales: {
                        xAxes: [{
                            ticks: {
                                beginAtZero: true
                            }
                        }]
                    }
                }
            });
        }
        else if (this.employmentTypes) {
               for (let i = 0; i < this.employmentTypes.length; i++) {
                label.push(this.employmentTypes[i].key);
                value.push(this.employmentTypes[i].doc_count);
                backgroundColor.push(this.getRandomColor());
            }

            const ctx = document.getElementById('employmentType-chart');

            new Chart(ctx, {
                type: 'horizontalBar',
                data: {
                    labels: label,
                    datasets: [{
                        data: value,
                        backgroundColor: backgroundColor
                    }]
                },
                options: {
                    legend: {
                        display: false
                    },
                    scales: {
                        xAxes: [{
                            ticks: {
                                beginAtZero: true
                            }
                        }]
                    }
                }
            });
        }
        else if (this.skills) {
               for (let i = 0; i < this.skills.length; i++) {
                label.push(this.skills[i].key);
                value.push(this.skills[i].doc_count);
                backgroundColor.push(this.getRandomColor());
            }

            const ctx = document.getElementById('skill-chart');

            new Chart(ctx, {
                type: 'horizontalBar',
                data: {
                    labels: label,
                    datasets: [{
                        data: value,
                        backgroundColor: backgroundColor
                    }]
                },
                options: {
                    legend: {
                        display: false
                    },
                    scales: {
                        xAxes: [{
                            ticks: {
                                beginAtZero: true
                            }
                        }]
                    }
                }
            });
        }
        else if (this.isRemote) {
               for (let i = 0; i < this.isRemote.length; i++) {
                label.push(this.isRemote[i].key);
                value.push(this.isRemote[i].doc_count);
                backgroundColor.push(this.getRandomColor());
            }

            const ctx = document.getElementById('remote-chart');

            new Chart(ctx, {
                type: 'horizontalBar',
                data: {
                    labels: label,
                    datasets: [{
                        data: value,
                        backgroundColor: backgroundColor
                    }]
                },
                options: {
                    legend: {
                        display: false
                    },
                    scales: {
                        xAxes: [{
                            ticks: {
                                beginAtZero: true
                            }
                        }]
                    }
                }
            });
        }
    },
    methods: {
        // Generate Random value of color for graph bar
        getRandomColor: function()  {
            var letters = '0123456789ABCDEF'.split('');
            var color = '#';
            for (var i = 0; i < 6; i++ ) {
                color += letters[Math.floor(Math.random() * 16)];
            }
            return color;
        }
    }
}
</script>

<style scoped>
    .ui.card {
        flex: 400px 1;
        margin: 10px;
    }
</style>