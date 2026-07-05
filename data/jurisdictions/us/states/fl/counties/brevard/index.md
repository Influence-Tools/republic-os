---
type: Jurisdiction
title: "Brevard County, FL"
classification: county
fips: "12009"
state: "FL"
demographics:
  population: 658447
  population_under_18: 130113
  population_18_64: 188809
  population_65_plus: 339525
  median_household_income: 78196
  poverty_rate: 9.96
  homeownership_rate: 76.7
  unemployment_rate: 5.08
  median_home_value: 372900
  gini_index: 0.4483
  vacancy_rate: 13.75
  race_white: 474039
  race_black: 67050
  race_asian: 17618
  race_native: 1128
  hispanic: 87618
  bachelors_plus: 250324
districts:
  - to: "us/states/fl/districts/08"
    rel: in-district
    area_weight: 0.8314
  - to: "us/states/fl/districts/senate/19"
    rel: in-district
    area_weight: 0.6281
  - to: "us/states/fl/districts/senate/8"
    rel: in-district
    area_weight: 0.2032
  - to: "us/states/fl/districts/house/31"
    rel: in-district
    area_weight: 0.2695
  - to: "us/states/fl/districts/house/33"
    rel: in-district
    area_weight: 0.1875
  - to: "us/states/fl/districts/house/32"
    rel: in-district
    area_weight: 0.1532
  - to: "us/states/fl/districts/house/30"
    rel: in-district
    area_weight: 0.1501
  - to: "us/states/fl/districts/house/34"
    rel: in-district
    area_weight: 0.0711
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, fl]
timestamp: "2026-07-03"
---

# Brevard County, FL

County jurisdiction — 102 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 658447 |
| Under 18 | 130113 |
| 18–64 | 188809 |
| 65+ | 339525 |
| Median household income | 78196 |
| Poverty rate | 9.96 |
| Homeownership rate | 76.7 |
| Unemployment rate | 5.08 |
| Median home value | 372900 |
| Gini index | 0.4483 |
| Vacancy rate | 13.75 |
| White | 474039 |
| Black | 67050 |
| Asian | 17618 |
| Native | 1128 |
| Hispanic/Latino | 87618 |
| Bachelor's or higher | 250324 |

## Districts

- [FL-08](/us/states/fl/districts/08.md) — 83% (congressional)
- [FL Senate District 19](/us/states/fl/districts/senate/19.md) — 63% (state senate)
- [FL Senate District 8](/us/states/fl/districts/senate/8.md) — 20% (state senate)
- [FL House District 31](/us/states/fl/districts/house/31.md) — 27% (state house)
- [FL House District 33](/us/states/fl/districts/house/33.md) — 19% (state house)
- [FL House District 32](/us/states/fl/districts/house/32.md) — 15% (state house)
- [FL House District 30](/us/states/fl/districts/house/30.md) — 15% (state house)
- [FL House District 34](/us/states/fl/districts/house/34.md) — 7% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
