export const calculatedTimePassed = (time) => {
  const now = new Date();
  const oldTime = new Date(time);

  const timeDifference = now - oldTime;

  const seconds = Math.floor(timeDifference / 1000);
  const minutes = Math.floor(seconds / 60);
  const hours = Math.floor(minutes / 60);
  const days = Math.floor(hours / 24);
  const weeks = Math.floor(days / 7);
  const months = Math.floor(days / 30);
  const years = Math.floor(months / 12);

  // if (years > 0) {
  //   return `${years} year${years === 1 ? "" : "s"} ago`;
  // } else if (months > 0) {
  //   return `${months} month${months === 1 ? "" : "s"} ago`;
  // } else if (weeks > 0) {
  //   return `${weeks} week${weeks === 1 ? "" : "s"} ago`;
  // } else if (days > 0) {
  //   return `${days} day${days === 1 ? "" : "s"} ago`;
  // } else if (hours > 0) {
  //   return `${hours} hour${hours === 1 ? "" : "s"} ago`;
  // } else if (minutes > 0) {
  //   return `${minutes} minute${minutes === 1 ? "" : "s"} ago`;
  // } else {
  //   return "Just now";
  // }

  if (years > 0) {
    return `${years}y ago`;
  } else if (months > 0) {
    return `${months}m ago`;
  } else if (weeks > 0) {
    return `${weeks}w ago`;
  } else if (days > 0) {
    return `${days}d ago`;
  } else if (hours > 0) {
    return `${hours}h ago`;
  } else if (minutes > 0) {
    return `${minutes}min ago`;
  } else {
    return "Just now";
  }
};
