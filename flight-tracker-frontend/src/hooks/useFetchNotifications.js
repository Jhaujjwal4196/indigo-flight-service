import { useRouter } from "next/router";
import { useEffect, useState } from "react";
import axios from "axios";

function useFetchNotifications() {
  const router = useRouter();
  const { query } = router;
  const [notifications, setNotifications] = useState([]);

  const queryParams = new URLSearchParams(query).toString();

  const getNotifications = async () => {
    const url = `http://localhost:8001/api/users/notifications?${queryParams}`;
    if (queryParams) {
      axios
        .get(url)
        .then((data) => {
          setNotifications(data?.data || []);
        })
        .catch((err) => console.error(err));
    }
  };

  useEffect(() => {
    getNotifications();
  }, [query]);

  return { getNotifications, notifications, setNotifications };
}

export default useFetchNotifications;
