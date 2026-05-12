import api from "../api/axios";

export const getDrills = async () => {

  const response = await api.get(
    "drills/"
  );

  return response.data;
};

export const createDrill = async (
  payload: any
) => {

  const response = await api.post(
    "drills/",
    payload
  );

  return response.data;
};