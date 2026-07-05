---
type: Jurisdiction
title: "Isle of Wight County, VA"
classification: county
fips: "51093"
state: "VA"
demographics:
  population: 39974
  population_under_18: 8502
  population_18_64: 23445
  population_65_plus: 8027
  median_household_income: 95241
  poverty_rate: 6.75
  homeownership_rate: 80.13
  unemployment_rate: 3.88
  median_home_value: 356500
  gini_index: 0.4302
  vacancy_rate: 7.99
  race_white: 27651
  race_black: 8543
  race_asian: 501
  race_native: 98
  hispanic: 1653
  bachelors_plus: 12121
districts:
  - to: "us/states/va/districts/02"
    rel: in-district
    area_weight: 0.8924
  - to: "us/states/va/districts/senate/17"
    rel: in-district
    area_weight: 0.8888
  - to: "us/states/va/districts/house/83"
    rel: in-district
    area_weight: 0.4895
  - to: "us/states/va/districts/house/84"
    rel: in-district
    area_weight: 0.3992
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Isle of Wight County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 39974 |
| Under 18 | 8502 |
| 18–64 | 23445 |
| 65+ | 8027 |
| Median household income | 95241 |
| Poverty rate | 6.75 |
| Homeownership rate | 80.13 |
| Unemployment rate | 3.88 |
| Median home value | 356500 |
| Gini index | 0.4302 |
| Vacancy rate | 7.99 |
| White | 27651 |
| Black | 8543 |
| Asian | 501 |
| Native | 98 |
| Hispanic/Latino | 1653 |
| Bachelor's or higher | 12121 |

## Districts

- [VA-02](/us/states/va/districts/02.md) — 89% (congressional)
- [VA Senate District 17](/us/states/va/districts/senate/17.md) — 89% (state senate)
- [VA House District 83](/us/states/va/districts/house/83.md) — 49% (state house)
- [VA House District 84](/us/states/va/districts/house/84.md) — 40% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
