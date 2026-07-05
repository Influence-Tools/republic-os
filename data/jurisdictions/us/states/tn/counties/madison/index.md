---
type: Jurisdiction
title: "Madison County, TN"
classification: county
fips: "47113"
state: "TN"
demographics:
  population: 99295
  population_under_18: 22287
  population_18_64: 59244
  population_65_plus: 17764
  median_household_income: 60042
  poverty_rate: 18.18
  homeownership_rate: 62.01
  unemployment_rate: 7.03
  median_home_value: 211800
  gini_index: 0.4688
  vacancy_rate: 8.93
  race_white: 53890
  race_black: 36004
  race_asian: 981
  race_native: 219
  hispanic: 5190
  bachelors_plus: 25091
districts:
  - to: "us/states/tn/districts/08"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tn/districts/senate/25"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tn/districts/house/73"
    rel: in-district
    area_weight: 0.7175
  - to: "us/states/tn/districts/house/80"
    rel: in-district
    area_weight: 0.2823
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Madison County, TN

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 99295 |
| Under 18 | 22287 |
| 18–64 | 59244 |
| 65+ | 17764 |
| Median household income | 60042 |
| Poverty rate | 18.18 |
| Homeownership rate | 62.01 |
| Unemployment rate | 7.03 |
| Median home value | 211800 |
| Gini index | 0.4688 |
| Vacancy rate | 8.93 |
| White | 53890 |
| Black | 36004 |
| Asian | 981 |
| Native | 219 |
| Hispanic/Latino | 5190 |
| Bachelor's or higher | 25091 |

## Districts

- [TN-08](/us/states/tn/districts/08.md) — 100% (congressional)
- [TN Senate District 25](/us/states/tn/districts/senate/25.md) — 100% (state senate)
- [TN House District 73](/us/states/tn/districts/house/73.md) — 72% (state house)
- [TN House District 80](/us/states/tn/districts/house/80.md) — 28% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
