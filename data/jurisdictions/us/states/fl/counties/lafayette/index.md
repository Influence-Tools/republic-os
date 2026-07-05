---
type: Jurisdiction
title: "Lafayette County, FL"
classification: county
fips: "12067"
state: "FL"
demographics:
  population: 8161
  population_under_18: 1414
  population_18_64: 4999
  population_65_plus: 1748
  median_household_income: 62757
  poverty_rate: 17.5
  homeownership_rate: 77.17
  unemployment_rate: 10.87
  median_home_value: 157200
  gini_index: 0.4064
  vacancy_rate: 21.36
  race_white: 5684
  race_black: 1441
  race_asian: 3
  race_native: 24
  hispanic: 1042
  bachelors_plus: 816
districts:
  - to: "us/states/fl/districts/03"
    rel: in-district
    area_weight: 0.9208
  - to: "us/states/fl/districts/02"
    rel: in-district
    area_weight: 0.0792
  - to: "us/states/fl/districts/senate/3"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/fl/districts/house/7"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, fl]
timestamp: "2026-07-03"
---

# Lafayette County, FL

County jurisdiction — 21 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 8161 |
| Under 18 | 1414 |
| 18–64 | 4999 |
| 65+ | 1748 |
| Median household income | 62757 |
| Poverty rate | 17.5 |
| Homeownership rate | 77.17 |
| Unemployment rate | 10.87 |
| Median home value | 157200 |
| Gini index | 0.4064 |
| Vacancy rate | 21.36 |
| White | 5684 |
| Black | 1441 |
| Asian | 3 |
| Native | 24 |
| Hispanic/Latino | 1042 |
| Bachelor's or higher | 816 |

## Districts

- [FL-03](/us/states/fl/districts/03.md) — 92% (congressional)
- [FL-02](/us/states/fl/districts/02.md) — 8% (congressional)
- [FL Senate District 3](/us/states/fl/districts/senate/3.md) — 100% (state senate)
- [FL House District 7](/us/states/fl/districts/house/7.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
