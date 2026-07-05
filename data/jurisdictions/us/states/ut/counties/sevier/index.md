---
type: Jurisdiction
title: "Sevier County, UT"
classification: county
fips: "49041"
state: "UT"
demographics:
  population: 22085
  population_under_18: 6144
  population_18_64: 12195
  population_65_plus: 3746
  median_household_income: 74884
  poverty_rate: 9.68
  homeownership_rate: 77.81
  unemployment_rate: 4.37
  median_home_value: 311200
  gini_index: 0.3818
  vacancy_rate: 15.04
  race_white: 20340
  race_black: 25
  race_asian: 72
  race_native: 152
  hispanic: 1171
  bachelors_plus: 4253
districts:
  - to: "us/states/ut/districts/02"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ut/districts/senate/27"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ut/districts/house/70"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ut]
timestamp: "2026-07-03"
---

# Sevier County, UT

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 22085 |
| Under 18 | 6144 |
| 18–64 | 12195 |
| 65+ | 3746 |
| Median household income | 74884 |
| Poverty rate | 9.68 |
| Homeownership rate | 77.81 |
| Unemployment rate | 4.37 |
| Median home value | 311200 |
| Gini index | 0.3818 |
| Vacancy rate | 15.04 |
| White | 20340 |
| Black | 25 |
| Asian | 72 |
| Native | 152 |
| Hispanic/Latino | 1171 |
| Bachelor's or higher | 4253 |

## Districts

- [UT-02](/us/states/ut/districts/02.md) — 100% (congressional)
- [UT Senate District 27](/us/states/ut/districts/senate/27.md) — 100% (state senate)
- [UT House District 70](/us/states/ut/districts/house/70.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
