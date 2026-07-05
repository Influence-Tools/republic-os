---
type: Jurisdiction
title: "Lake County, FL"
classification: county
fips: "12069"
state: "FL"
demographics:
  population: 412924
  population_under_18: 78465
  population_18_64: 224596
  population_65_plus: 109863
  median_household_income: 73161
  poverty_rate: 8.85
  homeownership_rate: 77.6
  unemployment_rate: 5.0
  median_home_value: 318400
  gini_index: 0.4324
  vacancy_rate: 12.31
  race_white: 277461
  race_black: 43228
  race_asian: 8527
  race_native: 641
  hispanic: 77473
  bachelors_plus: 115847
districts:
  - to: "us/states/fl/districts/11"
    rel: in-district
    area_weight: 0.5673
  - to: "us/states/fl/districts/06"
    rel: in-district
    area_weight: 0.4323
  - to: "us/states/fl/districts/senate/13"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/fl/districts/house/25"
    rel: in-district
    area_weight: 0.4287
  - to: "us/states/fl/districts/house/27"
    rel: in-district
    area_weight: 0.3053
  - to: "us/states/fl/districts/house/26"
    rel: in-district
    area_weight: 0.2657
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, fl]
timestamp: "2026-07-03"
---

# Lake County, FL

County jurisdiction — 84 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 412924 |
| Under 18 | 78465 |
| 18–64 | 224596 |
| 65+ | 109863 |
| Median household income | 73161 |
| Poverty rate | 8.85 |
| Homeownership rate | 77.6 |
| Unemployment rate | 5.0 |
| Median home value | 318400 |
| Gini index | 0.4324 |
| Vacancy rate | 12.31 |
| White | 277461 |
| Black | 43228 |
| Asian | 8527 |
| Native | 641 |
| Hispanic/Latino | 77473 |
| Bachelor's or higher | 115847 |

## Districts

- [FL-11](/us/states/fl/districts/11.md) — 57% (congressional)
- [FL-06](/us/states/fl/districts/06.md) — 43% (congressional)
- [FL Senate District 13](/us/states/fl/districts/senate/13.md) — 100% (state senate)
- [FL House District 25](/us/states/fl/districts/house/25.md) — 43% (state house)
- [FL House District 27](/us/states/fl/districts/house/27.md) — 31% (state house)
- [FL House District 26](/us/states/fl/districts/house/26.md) — 27% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
