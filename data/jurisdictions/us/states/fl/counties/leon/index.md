---
type: Jurisdiction
title: "Leon County, FL"
classification: county
fips: "12073"
state: "FL"
demographics:
  population: 297542
  population_under_18: 55054
  population_18_64: 198480
  population_65_plus: 44008
  median_household_income: 66287
  poverty_rate: 18.67
  homeownership_rate: 52.57
  unemployment_rate: 5.69
  median_home_value: 301800
  gini_index: 0.4992
  vacancy_rate: 11.03
  race_white: 164417
  race_black: 90396
  race_asian: 10580
  race_native: 396
  hispanic: 24307
  bachelors_plus: 125333
districts:
  - to: "us/states/fl/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/fl/districts/senate/3"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/fl/districts/house/9"
    rel: in-district
    area_weight: 0.5084
  - to: "us/states/fl/districts/house/7"
    rel: in-district
    area_weight: 0.3351
  - to: "us/states/fl/districts/house/8"
    rel: in-district
    area_weight: 0.1565
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, fl]
timestamp: "2026-07-03"
---

# Leon County, FL

County jurisdiction — 27 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 297542 |
| Under 18 | 55054 |
| 18–64 | 198480 |
| 65+ | 44008 |
| Median household income | 66287 |
| Poverty rate | 18.67 |
| Homeownership rate | 52.57 |
| Unemployment rate | 5.69 |
| Median home value | 301800 |
| Gini index | 0.4992 |
| Vacancy rate | 11.03 |
| White | 164417 |
| Black | 90396 |
| Asian | 10580 |
| Native | 396 |
| Hispanic/Latino | 24307 |
| Bachelor's or higher | 125333 |

## Districts

- [FL-02](/us/states/fl/districts/02.md) — 100% (congressional)
- [FL Senate District 3](/us/states/fl/districts/senate/3.md) — 100% (state senate)
- [FL House District 9](/us/states/fl/districts/house/9.md) — 51% (state house)
- [FL House District 7](/us/states/fl/districts/house/7.md) — 34% (state house)
- [FL House District 8](/us/states/fl/districts/house/8.md) — 16% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
