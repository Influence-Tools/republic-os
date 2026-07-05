---
type: Jurisdiction
title: "Elkhart County, IN"
classification: county
fips: "18039"
state: "IN"
demographics:
  population: 207132
  population_under_18: 56707
  population_18_64: 118482
  population_65_plus: 31943
  median_household_income: 68561
  poverty_rate: 12.4
  homeownership_rate: 71.57
  unemployment_rate: 3.6
  median_home_value: 210400
  gini_index: 0.4367
  vacancy_rate: 10.17
  race_white: 152453
  race_black: 10034
  race_asian: 2043
  race_native: 1349
  hispanic: 41619
  bachelors_plus: 36070
districts:
  - to: "us/states/in/districts/02"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/in/districts/senate/12"
    rel: in-district
    area_weight: 0.5299
  - to: "us/states/in/districts/senate/9"
    rel: in-district
    area_weight: 0.2686
  - to: "us/states/in/districts/senate/11"
    rel: in-district
    area_weight: 0.2013
  - to: "us/states/in/districts/house/49"
    rel: in-district
    area_weight: 0.3583
  - to: "us/states/in/districts/house/21"
    rel: in-district
    area_weight: 0.3111
  - to: "us/states/in/districts/house/48"
    rel: in-district
    area_weight: 0.1699
  - to: "us/states/in/districts/house/18"
    rel: in-district
    area_weight: 0.1604
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Elkhart County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 207132 |
| Under 18 | 56707 |
| 18–64 | 118482 |
| 65+ | 31943 |
| Median household income | 68561 |
| Poverty rate | 12.4 |
| Homeownership rate | 71.57 |
| Unemployment rate | 3.6 |
| Median home value | 210400 |
| Gini index | 0.4367 |
| Vacancy rate | 10.17 |
| White | 152453 |
| Black | 10034 |
| Asian | 2043 |
| Native | 1349 |
| Hispanic/Latino | 41619 |
| Bachelor's or higher | 36070 |

## Districts

- [IN-02](/us/states/in/districts/02.md) — 100% (congressional)
- [IN Senate District 12](/us/states/in/districts/senate/12.md) — 53% (state senate)
- [IN Senate District 9](/us/states/in/districts/senate/9.md) — 27% (state senate)
- [IN Senate District 11](/us/states/in/districts/senate/11.md) — 20% (state senate)
- [IN House District 49](/us/states/in/districts/house/49.md) — 36% (state house)
- [IN House District 21](/us/states/in/districts/house/21.md) — 31% (state house)
- [IN House District 48](/us/states/in/districts/house/48.md) — 17% (state house)
- [IN House District 18](/us/states/in/districts/house/18.md) — 16% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
