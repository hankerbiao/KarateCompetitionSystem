<template>
  <div>
    <div class="container">
      <el-input v-model="search" size="large" placeholder="搜索赛程名称" style="width: 300px;"/>
      <br/>
      <br/>
      <el-table :data="filterTableData" style="width: 100%">
        <el-table-column label="赛程名称" prop="name" align="center"/>
        <el-table-column label="场地名称" prop="site_name" align="center"/>
        <el-table-column label="比赛状态" align="center">
          <template #default="scope">
            <el-tag :type="scope.row.status === 0 ? 'info' : scope.row.status === 1 ? 'warning' : 'success'">
              {{ scope.row.status === 0 ? '未开始' : scope.row.status === 1 ? '比赛中' : '比赛完成' }}
            </el-tag>
          </template>
        </el-table-column>
        <el-table-column label="红方" prop="red_name" align="center"/>
        <el-table-column label="红方单位" prop="red_unit" align="center"/>
        <el-table-column label="红方得分" prop="red_score" align="center"/>
        <el-table-column label="红方犯规数" prop="red_foul" align="center"/>
        <el-table-column label="青方" prop="cyan_name" align="center"/>
        <el-table-column label="青方单位" prop="cyan_unit" align="center"/>
        <el-table-column label="青方得分" prop="cyan_score" align="center"/>
        <el-table-column label="青方犯规数" prop="cyan_foul" align="center"/>
        <el-table-column label="获胜方" prop="winner_id" align="center"/>
      </el-table>
    </div>
  </div>
</template>

<script lang="ts" setup>
import {computed, ref} from 'vue'
import {fetchDatas} from "@/api/index"

interface Schedule {
  id: number
  name: string
  site_id: number
  status: number
  red_score: number
  red_foul: number
  cyan_score: number
  cyan_foul: number
  video_path?: string
  red_id: number
  cyan_id: number
  red_name?: string
  cyan_name?: string
  red_unit?: string
  cyan_unit?: string
  site_name: string
  winner_id?: number
}

const search = ref('')
const tableData = ref<Schedule[]>([])

const filterTableData = computed(() =>
    tableData.value.filter(
        (data) =>
            !search.value || data.name.toLowerCase().includes(search.value.toLowerCase())
    )
)

const getData = async () => {
  const res = await fetchDatas('/api/v1/schedules/')
  tableData.value = res.data.data
  console.log(res.data)
}
getData()
</script>

