import api from "../api/axios";

export const getMaintenanceTasks = async (
  filters = ""
) => {

  const response = await api.get(
    `maintenance/${filters}`
  );

  return response.data;
};

export const createMaintenanceTask = async (
  payload: any
) => {

  const response = await api.post(
    "maintenance/",
    payload
  );

  return response.data;
};

export const updateMaintenanceTask = async (
  id: number,
  payload: any
) => {

  const response = await api.patch(
    `maintenance/${id}/`,
    payload
  );

  return response.data;
};