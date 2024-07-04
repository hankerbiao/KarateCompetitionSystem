<template>
  <el-form :model="form" label-width="auto" style="max-width: 1000px ">
    <el-form-item label="赛程名称：">
      <el-autocomplete
          v-model="scheduleName"
          :fetch-suggestions="querySearchName"
          clearable
          placeholder="Please Input"
          style="width: 300px; margin-right: auto;"
      />
    </el-form-item>
    <el-form-item label="选择场地：">
      <el-select v-model="form.field" placeholder="please select your zone" style="width: 300px; margin-right: auto;">
        <el-option
            v-for="option in options"
            :key="option.name"
            :label="option.name"
            :value="option.id"
        />
      </el-select>
    </el-form-item>
    <el-form-item label="红方运动员：">
      <el-autocomplete
          v-model="state_red"
          :fetch-suggestions="querySearch"
          clearable
          class="inline-input w-50"
          placeholder="Please Input"
          @select="handleSelectRed"
      />
      <el-text ref="redLabel" class="red-label" type="danger" style="margin-left: 20px"></el-text>
    </el-form-item>
    <el-form-item label="青方运动员：">
      <el-autocomplete
          v-model="state_cyan"
          :fetch-suggestions="querySearch"
          clearable
          class="inline-input w-50"
          placeholder="Please Input"
          @select="handleSelectCyan"
      />
      <el-text ref="cyanLabel" class="cyan-label" type="primary" style="margin-left: 20px"></el-text>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="onSubmit">Create</el-button>
      <el-button @click="onCancel">Cancel</el-button>
    </el-form-item>
  </el-form>
</template>

<script lang="ts" setup>
import {onMounted, reactive, ref} from 'vue'
import {createSchedule, fetchAthleteData, fetchDatas, fetchScheduleData} from "@/api";
import {resultProps} from "element-plus";

const options = ref([]);
const state_red = ref('')
const scheduleName = ref('')
const state_cyan = ref('')
const restaurants = ref<RestaurantItem[]>([])
const restaurantsName = ref<RestaurantItem[]>([])
const redLabel = ref(null);
const cyanLabel = ref(null);

const {update,cancel} = defineProps({
  update: {
    type: Function,
    required: true
  } ,
  cancel: {
    type: Function,
    required: true
  }
});
// do not use same name with ref
const form = reactive({
  name: '',
  field: '',
})

const onSubmit = async () => {
  console.log(form)
  // schema name
  console.log(scheduleName.value)
  // field_id
  console.log(form.field)
  // red id
  let red_id = undefined
  // cyan id
  let cyan_id = undefined
  for (let key in restaurants.value){
    if (restaurants.value[key].value == state_red.value){
      red_id = restaurants.value[key].id
    }
    if (restaurants.value[key].value == state_cyan.value){
      cyan_id = restaurants.value[key].id
    }
  }
  const data = {
    name:scheduleName.value,
    site_id:form.field,
    red_id:red_id,
    cyan_id:cyan_id,
    status:0
  }
  await createSchedule(data)

  update()  // 更新页面信息
}

const onCancel = () => {
  cancel()
}

interface RestaurantItem {
  value: string
  unit: string
  id: number
}

const querySearch = (queryString: string, cb: any) => {
  const results = queryString
      ? restaurants.value.filter(createFilter(queryString))
      : restaurants.value
  cb(results)
}


const querySearchName = (queryString: string, cb: any) => {
  const results = queryString
      ? restaurantsName.value.filter(createFilter(queryString))
      : restaurantsName.value
  cb(results)
}


const createFilter = (queryString: string) => {
  return (restaurant: RestaurantItem) => {
    return (
        restaurant.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0
    )
  }
}


const handleSelectRed = (item: RestaurantItem) => {
  if (redLabel.value) {
    redLabel.value.$el.innerText = item.unit;
  }
};

const handleSelectCyan = (item: RestaurantItem) => {
  if (cyanLabel.value) {
    cyanLabel.value.$el.innerText = item.unit;
  }
};

const fetchOptions = async () => {
  try {
    const res = await fetchDatas("/api/v1/fields/");
    options.value = res.data.data;
  } catch (error) {
    console.error('Error fetching options:', error);
  }
};

const fetchRestaurants = async () => {
  try {
    restaurants.value = await fetchAthleteData();
  } catch (error) {
    console.error('Error fetching restaurants:', error);
  }
};

const fetchRestaurantsScheduleName = async () => {
  try {
    restaurantsName.value = await fetchScheduleData();
  } catch (error) {
    console.error('Error fetching restaurants:', error);
  }
};



onMounted(async () => {
  await Promise.all([fetchOptions(), fetchRestaurants(),fetchRestaurantsScheduleName()]);
});
</script>
