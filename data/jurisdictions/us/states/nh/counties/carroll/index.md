---
type: Jurisdiction
title: "Carroll County, NH"
classification: county
fips: "33003"
state: "NH"
demographics:
  population: 51804
  population_under_18: 7631
  population_18_64: 28171
  population_65_plus: 16002
  median_household_income: 86463
  poverty_rate: 7.59
  homeownership_rate: 83.35
  unemployment_rate: 5.06
  median_home_value: 388900
  gini_index: 0.4611
  vacancy_rate: 45.95
  race_white: 48863
  race_black: 310
  race_asian: 427
  race_native: 219
  hispanic: 909
  bachelors_plus: 22713
districts:
  - to: "us/states/nh/districts/01"
    rel: in-district
    area_weight: 0.7596
  - to: "us/states/nh/districts/02"
    rel: in-district
    area_weight: 0.2401
  - to: "us/states/nh/districts/senate/3"
    rel: in-district
    area_weight: 0.905
  - to: "us/states/nh/districts/senate/2"
    rel: in-district
    area_weight: 0.0947
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nh]
timestamp: "2026-07-03"
---

# Carroll County, NH

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 51804 |
| Under 18 | 7631 |
| 18–64 | 28171 |
| 65+ | 16002 |
| Median household income | 86463 |
| Poverty rate | 7.59 |
| Homeownership rate | 83.35 |
| Unemployment rate | 5.06 |
| Median home value | 388900 |
| Gini index | 0.4611 |
| Vacancy rate | 45.95 |
| White | 48863 |
| Black | 310 |
| Asian | 427 |
| Native | 219 |
| Hispanic/Latino | 909 |
| Bachelor's or higher | 22713 |

## Districts

- [NH-01](/us/states/nh/districts/01.md) — 76% (congressional)
- [NH-02](/us/states/nh/districts/02.md) — 24% (congressional)
- [NH Senate District 3](/us/states/nh/districts/senate/3.md) — 90% (state senate)
- [NH Senate District 2](/us/states/nh/districts/senate/2.md) — 9% (state senate)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
