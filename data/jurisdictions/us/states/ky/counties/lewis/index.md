---
type: Jurisdiction
title: "Lewis County, KY"
classification: county
fips: "21135"
state: "KY"
demographics:
  population: 12965
  population_under_18: 2942
  population_18_64: 7496
  population_65_plus: 2527
  median_household_income: 46838
  poverty_rate: 22.03
  homeownership_rate: 79.18
  unemployment_rate: 6.04
  median_home_value: 96000
  gini_index: 0.4698
  vacancy_rate: 17.26
  race_white: 12559
  race_black: 70
  race_asian: 22
  race_native: 0
  hispanic: 15
  bachelors_plus: 2076
districts:
  - to: "us/states/ky/districts/04"
    rel: in-district
    area_weight: 0.9963
  - to: "us/states/ky/districts/senate/18"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/ky/districts/house/96"
    rel: in-district
    area_weight: 0.9992
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Lewis County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12965 |
| Under 18 | 2942 |
| 18–64 | 7496 |
| 65+ | 2527 |
| Median household income | 46838 |
| Poverty rate | 22.03 |
| Homeownership rate | 79.18 |
| Unemployment rate | 6.04 |
| Median home value | 96000 |
| Gini index | 0.4698 |
| Vacancy rate | 17.26 |
| White | 12559 |
| Black | 70 |
| Asian | 22 |
| Native | 0 |
| Hispanic/Latino | 15 |
| Bachelor's or higher | 2076 |

## Districts

- [KY-04](/us/states/ky/districts/04.md) — 100% (congressional)
- [KY Senate District 18](/us/states/ky/districts/senate/18.md) — 100% (state senate)
- [KY House District 96](/us/states/ky/districts/house/96.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
