---
type: Jurisdiction
title: "Green County, WI"
classification: county
fips: "55045"
state: "WI"
demographics:
  population: 37017
  population_under_18: 7954
  population_18_64: 21429
  population_65_plus: 7634
  median_household_income: 82852
  poverty_rate: 7.71
  homeownership_rate: 75.87
  unemployment_rate: 3.63
  median_home_value: 250200
  gini_index: 0.4072
  vacancy_rate: 4.28
  race_white: 34484
  race_black: 385
  race_asian: 264
  race_native: 30
  hispanic: 1567
  bachelors_plus: 9672
districts:
  - to: "us/states/wi/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/wi/districts/senate/17"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/wi/districts/house/50"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wi]
timestamp: "2026-07-03"
---

# Green County, WI

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 37017 |
| Under 18 | 7954 |
| 18–64 | 21429 |
| 65+ | 7634 |
| Median household income | 82852 |
| Poverty rate | 7.71 |
| Homeownership rate | 75.87 |
| Unemployment rate | 3.63 |
| Median home value | 250200 |
| Gini index | 0.4072 |
| Vacancy rate | 4.28 |
| White | 34484 |
| Black | 385 |
| Asian | 264 |
| Native | 30 |
| Hispanic/Latino | 1567 |
| Bachelor's or higher | 9672 |

## Districts

- [WI-02](/us/states/wi/districts/02.md) — 100% (congressional)
- [WI Senate District 17](/us/states/wi/districts/senate/17.md) — 100% (state senate)
- [WI House District 50](/us/states/wi/districts/house/50.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
