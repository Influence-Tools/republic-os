---
type: Jurisdiction
title: "Natchitoches Parish, LA"
classification: county
fips: "22069"
state: "LA"
demographics:
  population: 36693
  population_under_18: 8400
  population_18_64: 22023
  population_65_plus: 6270
  median_household_income: 46292
  poverty_rate: 25.42
  homeownership_rate: 60.95
  unemployment_rate: 5.61
  median_home_value: 171300
  gini_index: 0.5098
  vacancy_rate: 22.61
  race_white: 18727
  race_black: 14552
  race_asian: 241
  race_native: 373
  hispanic: 1438
  bachelors_plus: 7905
districts:
  - to: "us/states/la/districts/06"
    rel: in-district
    area_weight: 0.9973
  - to: "us/states/la/districts/senate/31"
    rel: in-district
    area_weight: 0.9681
  - to: "us/states/la/districts/senate/29"
    rel: in-district
    area_weight: 0.0319
  - to: "us/states/la/districts/house/25"
    rel: in-district
    area_weight: 0.6781
  - to: "us/states/la/districts/house/13"
    rel: in-district
    area_weight: 0.2959
  - to: "us/states/la/districts/house/22"
    rel: in-district
    area_weight: 0.0258
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, la]
timestamp: "2026-07-03"
---

# Natchitoches Parish, LA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 36693 |
| Under 18 | 8400 |
| 18–64 | 22023 |
| 65+ | 6270 |
| Median household income | 46292 |
| Poverty rate | 25.42 |
| Homeownership rate | 60.95 |
| Unemployment rate | 5.61 |
| Median home value | 171300 |
| Gini index | 0.5098 |
| Vacancy rate | 22.61 |
| White | 18727 |
| Black | 14552 |
| Asian | 241 |
| Native | 373 |
| Hispanic/Latino | 1438 |
| Bachelor's or higher | 7905 |

## Districts

- [LA-06](/us/states/la/districts/06.md) — 100% (congressional)
- [LA Senate District 31](/us/states/la/districts/senate/31.md) — 97% (state senate)
- [LA Senate District 29](/us/states/la/districts/senate/29.md) — 3% (state senate)
- [LA House District 25](/us/states/la/districts/house/25.md) — 68% (state house)
- [LA House District 13](/us/states/la/districts/house/13.md) — 30% (state house)
- [LA House District 22](/us/states/la/districts/house/22.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
