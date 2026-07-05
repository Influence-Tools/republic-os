---
type: Jurisdiction
title: "Nicholas County, KY"
classification: county
fips: "21181"
state: "KY"
demographics:
  population: 7708
  population_under_18: 1879
  population_18_64: 4530
  population_65_plus: 1299
  median_household_income: 59531
  poverty_rate: 17.57
  homeownership_rate: 74.5
  unemployment_rate: 6.09
  median_home_value: 123000
  gini_index: 0.3964
  vacancy_rate: 16.71
  race_white: 7413
  race_black: 91
  race_asian: 0
  race_native: 16
  hispanic: 80
  bachelors_plus: 750
districts:
  - to: "us/states/ky/districts/06"
    rel: in-district
    area_weight: 0.9945
  - to: "us/states/ky/districts/04"
    rel: in-district
    area_weight: 0.0055
  - to: "us/states/ky/districts/senate/27"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ky/districts/house/72"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Nicholas County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7708 |
| Under 18 | 1879 |
| 18–64 | 4530 |
| 65+ | 1299 |
| Median household income | 59531 |
| Poverty rate | 17.57 |
| Homeownership rate | 74.5 |
| Unemployment rate | 6.09 |
| Median home value | 123000 |
| Gini index | 0.3964 |
| Vacancy rate | 16.71 |
| White | 7413 |
| Black | 91 |
| Asian | 0 |
| Native | 16 |
| Hispanic/Latino | 80 |
| Bachelor's or higher | 750 |

## Districts

- [KY-06](/us/states/ky/districts/06.md) — 99% (congressional)
- [KY-04](/us/states/ky/districts/04.md) — 1% (congressional)
- [KY Senate District 27](/us/states/ky/districts/senate/27.md) — 100% (state senate)
- [KY House District 72](/us/states/ky/districts/house/72.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
