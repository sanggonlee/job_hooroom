<template>
    <div v-if="locations" class="ui fluid card">
        <div class="content">
            <h5 class="header">Locations</h5>
            <p class="card-text">Source:</p>
            <canvas id="location-chart"></canvas>
        </div>
    </div>
    <div v-else-if="employmentTypes" class="ui fluid card">
        <div class="content">
            <h5 class="header">Employment Types</h5>
            <p class="card-text">Source:</p>
            <canvas id="employmentType-chart"></canvas>
        </div>
    </div>
    <div v-else-if="skills" class="ui fluid card">
        <div class="content">
            <h5 class="header">Skills</h5>
            <p class="card-text">Source:</p>
            <canvas id="skill-chart"></canvas>
        </div>
    </div>
    <div v-else-if="isRemote" class="ui fluid card">
        <div class="content">
            <h5 class="header">Remote Eligible</h5>
            <p class="card-text">Source:</p>
            <canvas id="remote-chart"></canvas>
        </div>
    </div>
</template>

<script>
import Chart from 'chart.js';

export default {
    name: 'CardListItem',
    props: ['locations', 'employmentTypes', 'skills', 'isRemote'],
    updated() {
        let label = [];
        let value = [];
        
        if (this.locations) {
            for (let i = 0; i < this.locations.length; i++) {
                label.push(this.locations[i].key);
                value.push(this.locations[i].doc_count);
            }

            const ctx = document.getElementById('location-chart');

            new Chart(ctx, {
                type: 'horizontalBar',
                data: {
                    labels: label,
                    datasets: [{
                        label: 'Job numbers by location',
                        data: value
                    }]
                },
                options: {
                    scales: {
                        yAexs: [{
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
            }

            const ctx = document.getElementById('employmentType-chart');

            new Chart(ctx, {
                type: 'horizontalBar',
                data: {
                    labels: label,
                    datasets: [{
                        label: 'Job numbers by Employment Types',
                        data: value
                    }]
                },
                options: {
                    scales: {
                        yAexs: [{
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
            }

            const ctx = document.getElementById('skill-chart');

            new Chart(ctx, {
                type: 'horizontalBar',
                data: {
                    labels: label,
                    datasets: [{
                        label: 'Job numbers by Skills',
                        data: value
                    }]
                },
                options: {
                    scales: {
                        yAexs: [{
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
            }

            const ctx = document.getElementById('remote-chart');

            new Chart(ctx, {
                type: 'horizontalBar',
                data: {
                    labels: label,
                    datasets: [{
                        label: 'Job numbers by Remote Eligible',
                        data: value
                    }]
                },
                options: {
                    scales: {
                        yAexs: [{
                            ticks: {
                                beginAtZero: true
                            }
                        }]
                    }
                }
            });
        }
    }
}
</script>

<style scoped>
    .cardList {
        width: 80%;
        margin: auto !important;
    }
    .card {
        float: left;
        width: 45% !important;
        margin: 10px;
    }
</style>