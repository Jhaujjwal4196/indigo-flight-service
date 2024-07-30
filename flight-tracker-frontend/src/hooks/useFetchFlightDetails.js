import { useRouter } from "next/router";
import { useEffect, useState } from "react";
import axios from "axios";

function useFetchFlightDetails() {
  const router = useRouter();
  const { query } = router;
  const [flightData, setFlightData] = useState([]);

  const queryParams = new URLSearchParams(query).toString();

  const getFlightData = async () => {
    const url = `http://localhost:8002/api/flights?${queryParams}`;
    if (queryParams) {
      axios
        .get(url)
        .then((data) => {
          setFlightData(data?.data || []);
        })
        .catch((err) => console.error(err));
    }
  };

  useEffect(() => {
    getFlightData();
  }, [query]);

  return { getFlightData, flightData, setFlightData };
}

export default useFetchFlightDetails;
