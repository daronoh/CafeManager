import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL;

export const fetchCafes = async (data) => {
    const location = data.queryKey[1] || '';
    const response = await axios.get(`${API_URL}/cafes?location=${location}`);
    return response.data;
};

export const fetchEmployees = async (data) => {
    const cafeName = data.queryKey[1] || '';
    const response = await axios.get(`${API_URL}/employees?cafe_name=${cafeName}`);
    return response.data;
};

export const addCafe = async (cafeData) => {
    const response = await axios.post(`${API_URL}/cafes`, cafeData);
    return response.data;
};

export const updateCafe = async (data) => {
    const response = await axios.put(`${API_URL}/cafes/${data.cafeId}`, data.cafeData);
    return response.data;
};

export const deleteCafe = async (cafeId) => {
    await axios.delete(`${API_URL}/cafes/${cafeId}`);
};

export const addEmployee = async (employeeData) => {
    const response = await axios.post(`${API_URL}/employees`, employeeData);
    return response.data;
};

export const updateEmployee = async (data) => {
    const response = await axios.put(`${API_URL}/employees/${data.employeeId}`, data.employeeData);
    return response.data;
};

export const deleteEmployee = async (employeeId) => {
    await axios.delete(`${API_URL}/employees/${employeeId}`);
};