import i18n from "i18next";
import translationEn from "./en/translation.json";
import translationDe from "./de/translation.json";
import detector from "i18next-browser-languagedetector";
import { initReactI18next } from "react-i18next";

export const resources = {
  en: {
    translation: translationEn,
  },
  de: {
    translation: translationDe,
  },
} as const;

i18n
  .use(detector)
  .use(initReactI18next)
  .init({
    resources,
    fallbackLng: "en",
  })
  .catch((e) => console.log(e));
