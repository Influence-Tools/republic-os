---
type: Jurisdiction
title: "Belknap County, NH"
classification: county
fips: "33001"
state: "NH"
demographics:
  population: 64659
  population_under_18: 11189
  population_18_64: 37978
  population_65_plus: 15492
  median_household_income: 92783
  poverty_rate: 8.48
  homeownership_rate: 80.1
  unemployment_rate: 3.1
  median_home_value: 374900
  gini_index: 0.449
  vacancy_rate: 32.47
  race_white: 60232
  race_black: 342
  race_asian: 744
  race_native: 20
  hispanic: 1467
  bachelors_plus: 23017
districts:
  - to: "us/states/nh/districts/01"
    rel: in-district
    area_weight: 0.8826
  - to: "us/states/nh/districts/02"
    rel: in-district
    area_weight: 0.1174
  - to: "us/states/nh/districts/senate/2"
    rel: in-district
    area_weight: 0.5753
  - to: "us/states/nh/districts/senate/6"
    rel: in-district
    area_weight: 0.3036
  - to: "us/states/nh/districts/senate/17"
    rel: in-district
    area_weight: 0.0953
  - to: "us/states/nh/districts/senate/7"
    rel: in-district
    area_weight: 0.0255
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nh]
timestamp: "2026-07-03"
---

# Belknap County, NH

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 64659 |
| Under 18 | 11189 |
| 18–64 | 37978 |
| 65+ | 15492 |
| Median household income | 92783 |
| Poverty rate | 8.48 |
| Homeownership rate | 80.1 |
| Unemployment rate | 3.1 |
| Median home value | 374900 |
| Gini index | 0.449 |
| Vacancy rate | 32.47 |
| White | 60232 |
| Black | 342 |
| Asian | 744 |
| Native | 20 |
| Hispanic/Latino | 1467 |
| Bachelor's or higher | 23017 |

## Districts

- [NH-01](/us/states/nh/districts/01.md) — 88% (congressional)
- [NH-02](/us/states/nh/districts/02.md) — 12% (congressional)
- [NH Senate District 2](/us/states/nh/districts/senate/2.md) — 58% (state senate)
- [NH Senate District 6](/us/states/nh/districts/senate/6.md) — 30% (state senate)
- [NH Senate District 17](/us/states/nh/districts/senate/17.md) — 10% (state senate)
- [NH Senate District 7](/us/states/nh/districts/senate/7.md) — 3% (state senate)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
