import request from '../utils/request';

export const fetchDatas = (url) => {
    return request({
        url,
        method: 'get'
    }).then(response => {
        return response;
    }).catch(error => {
        console.error('Error fetching athletes:', error);
        throw error;
    });
};

export const postData = (url, data) => {
    return request({
        url,
        method: 'post',
        data
    }).then(response => {
        return response;
    }).catch(error => {
        console.error('Error posting data:', error);
        throw error;
    });
};

export const deleteData = (url) => {
    return request({
        url,
        method: 'delete'
    }).then(response => {
        return response;
    }).catch(error => {
        console.error('Error deleting data:', error);
        throw error;
    });
};

export const deleteSchedule = async (schedule_id) => {
    const url = `/api/v1/schedules/${schedule_id}`;
    return deleteData(url)
};


export const deleteField = async (field_id) => {
    const url = `/api/v1/fields/${field_id}`;
    return deleteData(url)
};

export const createSchedule = async (data) => {
    const url = "/api/v1/schedules"
    return postData(url, data)
}


export const fetchUserData = () => {
    return request({
        url: './mock/user.json',
        method: 'get'
    });
};


// 查询所有运动员姓名、单位、id
export const fetchAthleteData = async () => {
    let result = [];
    try {
        const res = await fetchDatas('/api/v1/athlete/');
        let data = res.data.data
        for (let key in data) {
            let obj = {}
            obj['value'] = data[key].name
            obj['id'] = data[key].id
            obj['unit'] = data[key].unit
            result.push(obj)
        }
        return result
    } catch (error) {
        console.error('Error in fetchAthleteData:', error);
    }
};

// 查询所有运动员姓名、单位、id
export const fetchScheduleData = async () => {
    let result = [];
    try {
        const res = await fetchDatas('/api/v1/schedules/schedules_name_list/');
        let data = res.data.data
        for (let key in data) {
            let obj = {}
            obj['value'] = data[key]
            result.push(obj)
        }
        console.log(result)
        return result
    } catch (error) {
        console.error('Error in fetchAthleteData:', error);
    }
};

export const fetchFieldData = async () => {
    try {
        const res = await fetchDatas('/api/v1/fields')
        return res.data.data
    } catch (error) {
        console.error('Error in fetchFieldData:', error);

    }
}