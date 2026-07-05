---
type: Jurisdiction
title: "Park County, WY"
classification: county
fips: "56029"
state: "WY"
demographics:
  population: 30449
  population_under_18: 6299
  population_18_64: 16410
  population_65_plus: 7740
  median_household_income: 73035
  poverty_rate: 8.91
  homeownership_rate: 75.33
  unemployment_rate: 2.2
  median_home_value: 400500
  gini_index: 0.4551
  vacancy_rate: 11.07
  race_white: 26889
  race_black: 74
  race_asian: 137
  race_native: 157
  hispanic: 1828
  bachelors_plus: 11016
districts:
  - to: "us/states/wy/districts/00"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/wy/districts/senate/18"
    rel: in-district
    area_weight: 0.7534
  - to: "us/states/wy/districts/senate/20"
    rel: in-district
    area_weight: 0.2083
  - to: "us/states/wy/districts/senate/19"
    rel: in-district
    area_weight: 0.0382
  - to: "us/states/wy/districts/house/24"
    rel: in-district
    area_weight: 0.5206
  - to: "us/states/wy/districts/house/50"
    rel: in-district
    area_weight: 0.2328
  - to: "us/states/wy/districts/house/28"
    rel: in-district
    area_weight: 0.2083
  - to: "us/states/wy/districts/house/26"
    rel: in-district
    area_weight: 0.0283
  - to: "us/states/wy/districts/house/25"
    rel: in-district
    area_weight: 0.0099
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wy]
timestamp: "2026-07-03"
---

# Park County, WY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 30449 |
| Under 18 | 6299 |
| 18–64 | 16410 |
| 65+ | 7740 |
| Median household income | 73035 |
| Poverty rate | 8.91 |
| Homeownership rate | 75.33 |
| Unemployment rate | 2.2 |
| Median home value | 400500 |
| Gini index | 0.4551 |
| Vacancy rate | 11.07 |
| White | 26889 |
| Black | 74 |
| Asian | 137 |
| Native | 157 |
| Hispanic/Latino | 1828 |
| Bachelor's or higher | 11016 |

## Districts

- [WY-00](/us/states/wy/districts/00.md) — 100% (congressional)
- [WY Senate District 18](/us/states/wy/districts/senate/18.md) — 75% (state senate)
- [WY Senate District 20](/us/states/wy/districts/senate/20.md) — 21% (state senate)
- [WY Senate District 19](/us/states/wy/districts/senate/19.md) — 4% (state senate)
- [WY House District 24](/us/states/wy/districts/house/24.md) — 52% (state house)
- [WY House District 50](/us/states/wy/districts/house/50.md) — 23% (state house)
- [WY House District 28](/us/states/wy/districts/house/28.md) — 21% (state house)
- [WY House District 26](/us/states/wy/districts/house/26.md) — 3% (state house)
- [WY House District 25](/us/states/wy/districts/house/25.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
