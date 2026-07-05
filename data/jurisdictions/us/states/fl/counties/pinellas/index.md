---
type: Jurisdiction
title: "Pinellas County, FL"
classification: county
fips: "12103"
state: "FL"
demographics:
  population: 963481
  population_under_18: 148581
  population_18_64: 560652
  population_65_plus: 254248
  median_household_income: 72646
  poverty_rate: 11.54
  homeownership_rate: 69.53
  unemployment_rate: 4.43
  median_home_value: 355100
  gini_index: 0.4881
  vacancy_rate: 17.62
  race_white: 708809
  race_black: 92541
  race_asian: 35302
  race_native: 2454
  hispanic: 108089
  bachelors_plus: 379379
districts:
  - to: "us/states/fl/districts/13"
    rel: in-district
    area_weight: 0.3238
  - to: "us/states/fl/districts/14"
    rel: in-district
    area_weight: 0.0602
  - to: "us/states/fl/districts/senate/18"
    rel: in-district
    area_weight: 0.1991
  - to: "us/states/fl/districts/senate/21"
    rel: in-district
    area_weight: 0.1481
  - to: "us/states/fl/districts/senate/16"
    rel: in-district
    area_weight: 0.0288
  - to: "us/states/fl/districts/house/57"
    rel: in-district
    area_weight: 0.1062
  - to: "us/states/fl/districts/house/61"
    rel: in-district
    area_weight: 0.0749
  - to: "us/states/fl/districts/house/60"
    rel: in-district
    area_weight: 0.0654
  - to: "us/states/fl/districts/house/58"
    rel: in-district
    area_weight: 0.0559
  - to: "us/states/fl/districts/house/59"
    rel: in-district
    area_weight: 0.0529
  - to: "us/states/fl/districts/house/62"
    rel: in-district
    area_weight: 0.0207
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, fl]
timestamp: "2026-07-03"
---

# Pinellas County, FL

County jurisdiction — 152 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 963481 |
| Under 18 | 148581 |
| 18–64 | 560652 |
| 65+ | 254248 |
| Median household income | 72646 |
| Poverty rate | 11.54 |
| Homeownership rate | 69.53 |
| Unemployment rate | 4.43 |
| Median home value | 355100 |
| Gini index | 0.4881 |
| Vacancy rate | 17.62 |
| White | 708809 |
| Black | 92541 |
| Asian | 35302 |
| Native | 2454 |
| Hispanic/Latino | 108089 |
| Bachelor's or higher | 379379 |

## Districts

- [FL-13](/us/states/fl/districts/13.md) — 32% (congressional)
- [FL-14](/us/states/fl/districts/14.md) — 6% (congressional)
- [FL Senate District 18](/us/states/fl/districts/senate/18.md) — 20% (state senate)
- [FL Senate District 21](/us/states/fl/districts/senate/21.md) — 15% (state senate)
- [FL Senate District 16](/us/states/fl/districts/senate/16.md) — 3% (state senate)
- [FL House District 57](/us/states/fl/districts/house/57.md) — 11% (state house)
- [FL House District 61](/us/states/fl/districts/house/61.md) — 7% (state house)
- [FL House District 60](/us/states/fl/districts/house/60.md) — 7% (state house)
- [FL House District 58](/us/states/fl/districts/house/58.md) — 6% (state house)
- [FL House District 59](/us/states/fl/districts/house/59.md) — 5% (state house)
- [FL House District 62](/us/states/fl/districts/house/62.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
