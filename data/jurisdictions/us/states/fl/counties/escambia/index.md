---
type: Jurisdiction
title: "Escambia County, FL"
classification: county
fips: "12033"
state: "FL"
demographics:
  population: 325923
  population_under_18: 79042
  population_18_64: 110459
  population_65_plus: 136422
  median_household_income: 67500
  poverty_rate: 14.71
  homeownership_rate: 64.78
  unemployment_rate: 5.87
  median_home_value: 257200
  gini_index: 0.4564
  vacancy_rate: 13.53
  race_white: 207088
  race_black: 68090
  race_asian: 9393
  race_native: 1254
  hispanic: 22701
  bachelors_plus: 89904
districts:
  - to: "us/states/fl/districts/01"
    rel: in-district
    area_weight: 0.6626
  - to: "us/states/fl/districts/senate/1"
    rel: in-district
    area_weight: 0.6625
  - to: "us/states/fl/districts/house/1"
    rel: in-district
    area_weight: 0.5055
  - to: "us/states/fl/districts/house/2"
    rel: in-district
    area_weight: 0.1569
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, fl]
timestamp: "2026-07-03"
---

# Escambia County, FL

County jurisdiction — 30 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 325923 |
| Under 18 | 79042 |
| 18–64 | 110459 |
| 65+ | 136422 |
| Median household income | 67500 |
| Poverty rate | 14.71 |
| Homeownership rate | 64.78 |
| Unemployment rate | 5.87 |
| Median home value | 257200 |
| Gini index | 0.4564 |
| Vacancy rate | 13.53 |
| White | 207088 |
| Black | 68090 |
| Asian | 9393 |
| Native | 1254 |
| Hispanic/Latino | 22701 |
| Bachelor's or higher | 89904 |

## Districts

- [FL-01](/us/states/fl/districts/01.md) — 66% (congressional)
- [FL Senate District 1](/us/states/fl/districts/senate/1.md) — 66% (state senate)
- [FL House District 1](/us/states/fl/districts/house/1.md) — 51% (state house)
- [FL House District 2](/us/states/fl/districts/house/2.md) — 16% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
