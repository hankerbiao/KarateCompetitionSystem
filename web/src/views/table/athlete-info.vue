<template>
  <div>
    <div class="container">
      <el-input v-model="search" size="large" placeholder="搜索运动员姓名/单位" style="width: 300px;"/>
      <br/>
      <br/>
      <el-table :data="filterTableData" style="width: 100%">
        <el-table-column label="姓名" prop="name" align="center"/>
        <el-table-column label="单位" prop="unit" align="center"/>
        <el-table-column label="组别(公斤级)" prop="group" align="center"/>
        <el-table-column label="当前名次" align="center">
          <template #default="scope">
            <el-tag :type="scope.row.place!= -1 ? 'success':'danger' ">
              {{ scope.row.place != -1 ? scope.row.place : "已淘汰" }}
            </el-tag>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script lang="ts" setup>
import {computed, ref} from 'vue'
import {fetchDatas} from "@/api/index"

interface Athlete {
  name: string
  unit: string
  group: string
  place: number
}

const search = ref('')
const tableData = ref<Athlete[]>([])

const filterTableData = computed(() =>
    tableData.value.filter(
        (data) =>
            !search.value || data.name.toLowerCase().includes(search.value.toLowerCase()) || data.unit.toLowerCase().includes(search.value.toLowerCase())
    )
)

const getData = async () => {
  try {
    const res = await fetchDatas(`/api/v1/athlete/`);
    tableData.value = res.data.data;
  } catch (error) {
    console.error('Error fetching data:', error);
  }
};

// Call getData every 10 seconds (10000 milliseconds)
setInterval(getData, 10000);

// Optionally, you can call getData immediately to fetch data right away
getData();

</script>

<style scoped>
</style>
