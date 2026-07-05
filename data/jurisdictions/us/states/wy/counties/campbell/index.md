---
type: Jurisdiction
title: "Campbell County, WY"
classification: county
fips: "56005"
state: "WY"
demographics:
  population: 47240
  population_under_18: 12606
  population_18_64: 28480
  population_65_plus: 6154
  median_household_income: 89869
  poverty_rate: 9.44
  homeownership_rate: 77.67
  unemployment_rate: 3.54
  median_home_value: 279100
  gini_index: 0.4092
  vacancy_rate: 10.16
  race_white: 40501
  race_black: 157
  race_asian: 115
  race_native: 612
  hispanic: 4562
  bachelors_plus: 10035
districts:
  - to: "us/states/wy/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/wy/districts/senate/23"
    rel: in-district
    area_weight: 0.5343
  - to: "us/states/wy/districts/senate/1"
    rel: in-district
    area_weight: 0.4629
  - to: "us/states/wy/districts/house/3"
    rel: in-district
    area_weight: 0.5323
  - to: "us/states/wy/districts/house/52"
    rel: in-district
    area_weight: 0.4629
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wy]
timestamp: "2026-07-03"
---

# Campbell County, WY

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 47240 |
| Under 18 | 12606 |
| 18–64 | 28480 |
| 65+ | 6154 |
| Median household income | 89869 |
| Poverty rate | 9.44 |
| Homeownership rate | 77.67 |
| Unemployment rate | 3.54 |
| Median home value | 279100 |
| Gini index | 0.4092 |
| Vacancy rate | 10.16 |
| White | 40501 |
| Black | 157 |
| Asian | 115 |
| Native | 612 |
| Hispanic/Latino | 4562 |
| Bachelor's or higher | 10035 |

## Districts

- [WY-00](/us/states/wy/districts/00.md) — 100% (congressional)
- [WY Senate District 23](/us/states/wy/districts/senate/23.md) — 53% (state senate)
- [WY Senate District 1](/us/states/wy/districts/senate/1.md) — 46% (state senate)
- [WY House District 3](/us/states/wy/districts/house/3.md) — 53% (state house)
- [WY House District 52](/us/states/wy/districts/house/52.md) — 46% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
