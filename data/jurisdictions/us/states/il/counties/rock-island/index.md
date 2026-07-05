---
type: Jurisdiction
title: "Rock Island County, IL"
classification: county
fips: "17161"
state: "IL"
demographics:
  population: 142757
  population_under_18: 32091
  population_18_64: 81605
  population_65_plus: 29061
  median_household_income: 67159
  poverty_rate: 15.5
  homeownership_rate: 69.66
  unemployment_rate: 5.6
  median_home_value: 150400
  gini_index: 0.4413
  vacancy_rate: 7.53
  race_white: 102074
  race_black: 16270
  race_asian: 3943
  race_native: 555
  hispanic: 20305
  bachelors_plus: 33089
districts:
  - to: "us/states/il/districts/17"
    rel: in-district
    area_weight: 0.9986
  - to: "us/states/il/districts/senate/47"
    rel: in-district
    area_weight: 0.4107
  - to: "us/states/il/districts/senate/36"
    rel: in-district
    area_weight: 0.3354
  - to: "us/states/il/districts/senate/37"
    rel: in-district
    area_weight: 0.2535
  - to: "us/states/il/districts/house/94"
    rel: in-district
    area_weight: 0.4107
  - to: "us/states/il/districts/house/73"
    rel: in-district
    area_weight: 0.2535
  - to: "us/states/il/districts/house/72"
    rel: in-district
    area_weight: 0.1775
  - to: "us/states/il/districts/house/71"
    rel: in-district
    area_weight: 0.1579
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Rock Island County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 142757 |
| Under 18 | 32091 |
| 18–64 | 81605 |
| 65+ | 29061 |
| Median household income | 67159 |
| Poverty rate | 15.5 |
| Homeownership rate | 69.66 |
| Unemployment rate | 5.6 |
| Median home value | 150400 |
| Gini index | 0.4413 |
| Vacancy rate | 7.53 |
| White | 102074 |
| Black | 16270 |
| Asian | 3943 |
| Native | 555 |
| Hispanic/Latino | 20305 |
| Bachelor's or higher | 33089 |

## Districts

- [IL-17](/us/states/il/districts/17.md) — 100% (congressional)
- [IL Senate District 47](/us/states/il/districts/senate/47.md) — 41% (state senate)
- [IL Senate District 36](/us/states/il/districts/senate/36.md) — 34% (state senate)
- [IL Senate District 37](/us/states/il/districts/senate/37.md) — 25% (state senate)
- [IL House District 94](/us/states/il/districts/house/94.md) — 41% (state house)
- [IL House District 73](/us/states/il/districts/house/73.md) — 25% (state house)
- [IL House District 72](/us/states/il/districts/house/72.md) — 18% (state house)
- [IL House District 71](/us/states/il/districts/house/71.md) — 16% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
